from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list),
    path('product-details/<int:id>/', views.product_details),
]