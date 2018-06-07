from django.urls import path

from . import views

urlpatterns = [
    path('', views.LandingPage, name='LandingPage'),
    path('prestations', views.Prestations, name='Prestations'),
    path('portfolio', views.Portfolio, name='Portfolio'),
    path('contact', views.Contact, name='Contact'),
    path('license', views.License, name='License'),
    path('home', views.Home, name='Home'),
]