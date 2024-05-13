from django.urls import path
from . import views

urlpatterns = [
    # path('new/', views.new, name='new'),
    # path('tees/', views.tees, name='tees'),
    # path('hoodies/', views.hoodies, name='hoodies'),
    path('garment/<product_id>/', views.garment, name='garment'),
    path('all_garments/', views.all_garments, name='all_garments'),
]
