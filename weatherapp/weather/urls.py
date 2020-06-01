from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<city_name>/', views.deletecity, name='deletecity')
]   