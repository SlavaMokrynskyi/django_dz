from django.contrib import admin

from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'category']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)