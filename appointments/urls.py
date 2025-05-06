from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
