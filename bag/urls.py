from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.bag_add, name='bag_add'),
    path('delete/', views.bag_delete, name='bag_delete'),
    path('update/', views.bag_update, name='bag_update'),
]
