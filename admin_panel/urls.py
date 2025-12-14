from django.urls import path
from admin_panel import views

urlpatterns = [
    path('', views.admin_panel),
    path('delete-product/<int:id>/', views.delete_product),
]