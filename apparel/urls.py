from django.urls import path
from . import views

urlpatterns = [
    path('garment/<int:product_id>/', views.garment, name='garment'),
    path('all_garments/', views.all_garments, name='all_garments'),
    path('add_garment/', views.add_garment, name='add_garment'),
    path('edit_garment/<int:product_id>/',
         views.edit_garment, name='edit_garment'),
    path('delete_garment/<int:product_id>/',
         views.delete_garment, name='delete_garment'),
]
