from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.place_list, name='place_list'),
    path('places/add/', views.add_place, name='add_place'),
    path('places/<int:index>/', views.place_detail, name='place_detail'),
]