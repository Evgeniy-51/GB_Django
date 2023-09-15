from django.contrib import admin

from homework.models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address", "reg_date")
    list_display_links = ("name", "email", "phone", "address")
    search_fields = ("name", "phone")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(Product)
