from homework.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about_me, name='about'),
    path('orders/<int:client_id>/', ShowOrdersByClientId.as_view(), name='orders'),
    path('week/<int:client_id>/', ShowOrdersForAWeek.as_view(), name='week'),
    path('month/<int:client_id>/', ShowOrdersForAMonth.as_view(), name='month'),
    path('year/<int:client_id>/', ShowOrdersForAYear.as_view(), name='year'),
    # path('change_prod/', change_product, name='change_product'),
    path('change_prod/<int:prod_id>/', change_product, name='change_product'),
]
