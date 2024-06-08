from django.urls import path
from . import views

urlpatterns = [
    path('garment/<int:product_id>/', views.garment, name='garment'),
    path('all_garments/', views.all_garments, name='all_garments'),
]
