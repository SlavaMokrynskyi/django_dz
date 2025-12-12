from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product-details', views.product_details, name='product_details'),
]