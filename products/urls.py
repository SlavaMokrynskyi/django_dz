from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product-details/<int:id>/', views.product_details, name='product_details'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('add-product/', views.add_product, name='add_product'),
]