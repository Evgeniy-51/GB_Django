from django.http import HttpResponse, HttpResponseRedirect
import logging
from datetime import datetime, timedelta
from django.views.generic import TemplateView
from homework.models import Order, Customer
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html_content = """
    <h1> Это мой первый </h1>
    <h2> Django сайт </h2>
    """
    return HttpResponse(html_content)


def about_me(request):
    logger.info('About page accessed')
    html_content = """
    <h1> Это страничка </h1>
    <h2> про меня </h2>
    """
    return HttpResponse(html_content)


class ShowOrdersByClientId(TemplateView):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            orders = Order.objects.filter(customer=client_id)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAWeek(TemplateView):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=7)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAMonth(ShowOrdersForAWeek):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=30)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context


class ShowOrdersForAYear(ShowOrdersForAWeek):
    template_name = "homework/show_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        if Customer.objects.filter(pk=client_id).exists():
            client = Customer.objects.get(pk=client_id)
            res_date = datetime.now().date() - timedelta(days=365)
            orders = Order.objects.filter(customer=client_id).filter(create_date__date__gt=res_date)
            context['name'] = client.name
            context['orders'] = orders
        return context
