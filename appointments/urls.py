from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('', views.index, name='index'),  # Add this for the main page
    path('dermatology/', views.dermatology, name='dermatology'),  # Add this for dermatology page
    path('plastic-surgery/', views.plastic_surgery, name='plastic-surgery'),
    path('skinandhairaesthetics/', views.skinandhairaesthetics, name='skinandhairaesthetics'),
    path('smile/', views.smile, name='smile'),
    path('obesity-clinic/', views.obesity_clinic, name='obesity-clinic'),
    path('cosmetic-gynecology/', views.cosmetic_gynecology, name='cosmetic-gynecology'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('thank-you/', views.thank_you, name='thank_you'),
]


