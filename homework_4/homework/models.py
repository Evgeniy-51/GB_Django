from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя")
    email = models.EmailField()
    phone = models.CharField(max_length=32, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ["reg_date", "name"]


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["title", "create_date"]


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product,  blank=True, related_name="products")
    quantity = models.PositiveSmallIntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk}, client  {self.customer}, sum {self.total_price}, products {self.products}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
