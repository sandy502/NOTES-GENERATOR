# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indextask, name='list'),
    path('update/<str:pk>/', views.updateTask, name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
