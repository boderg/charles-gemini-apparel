from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_arrivals, name='new_arrivals'),
]
