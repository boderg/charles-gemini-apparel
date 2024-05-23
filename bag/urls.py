from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.bag_add, name='bag_add'),
    path('update_or_delete/<item_id>/',
         views.bag_update_or_delete, name='bag_update_or_delete'),
]
