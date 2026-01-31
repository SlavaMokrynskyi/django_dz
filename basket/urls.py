from django.urls import path

from basket import views

urlpatterns = [
    path('', views.index, name='basket'),
    path('add/<int:product_id>/', views.add_product, name='add_basket_product'),
    path('remove/<int:product_id>/', views.remove_product, name='remove_basket_product'),
]
