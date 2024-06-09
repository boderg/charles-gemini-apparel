from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('newsletter_signup/', views.newsletter_signup,
         name='newsletter_signup'),
    path('newsletter_success/', views.newsletter_success,
         name='newsletter_success'),
]
