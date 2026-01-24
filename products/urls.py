from django.urls import path
from django.contrib import admin
from products import views

urlpatterns = [
    path('product-details/<int:id>/', views.product_details, name='product_details'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('add-product/', views.add_product, name='add_product'),
    path('update-product/<int:id>/', views.update_product, name='update_product'),
]
    