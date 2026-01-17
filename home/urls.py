from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', views.index, {'filter_by_favorites': True}, name='favorites'),
]
