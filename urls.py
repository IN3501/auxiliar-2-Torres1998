from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pestana/', views.pestana, name='pestana'),
    path('desafio2/', views.desafio2, name='desafio2'),
]
