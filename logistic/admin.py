from django.contrib import admin
from logistic.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
