from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),

    path('add_garment/', views.add_garment, name='add_garment'),
    path('edit_garment/<int:product_id>/',
         views.edit_garment, name='edit_garment'),
    path('list_garments/', views.list_garments, name='list_garments'),
    path('delete_garment/<int:product_id>/',
         views.delete_garment, name='delete_garment'),

    path('add_colour/', views.add_colour, name='add_colour'),
    path('edit_colour/<int:colour_id>/',
         views.edit_colour, name='edit_colour'),
    path('list_colours/', views.list_colours, name='list_colours'),
    path('delete_colour/<int:colour_id>/',
         views.delete_colour, name='delete_colour'),

    path('add_size/', views.add_size, name='add_size'),
    path('edit_size/<int:size_id>/', views.edit_size, name='edit_size'),
    path('list_sizes/', views.list_sizes, name='list_sizes'),
    path('delete_size/<int:size_id>/', views.delete_size, name='delete_size'),
]
