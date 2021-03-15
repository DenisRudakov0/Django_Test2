from django.urls import path
from . import views

urlpatterns = [
    # При переходе будет открываться панель администратора
    # Отслеживание url адресов
    path('', views.index),
    path('about', views.about),
]
