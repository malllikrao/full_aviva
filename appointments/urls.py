from django.urls import path
from . import views
from django.shortcuts import redirect



urlpatterns = [

    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
     #path('', frontend, name='frontend'),
    path('', lambda request: redirect('book_appointment')),
    path('book/', views.book_appointment, name='book_appointment'),
    path('thank-you/', views.thank_you, name='thank_you'),
]

#from django.urls import path
#from .views import book_appointment, thank_you, frontend

#urlpatterns = [
    #path('', frontend, name='frontend'),  # main frontend page
    ##path('book/', book_appointment, name='book_appointment'),
    #path('thank-you/', thank_you, name='thank_you'),
#]