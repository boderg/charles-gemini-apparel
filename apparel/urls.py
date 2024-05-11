from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('tees/', views.tees, name='tees'),
    path('hoodies/', views.hoodies, name='hoodies'),
    path('garment/<product_id>/', views.garment, name='garment'),
]
