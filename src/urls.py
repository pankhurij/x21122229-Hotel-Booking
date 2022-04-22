from django.urls import path
from .views import *



urlpatterns = [
    
    path('', home, name='home'),
    path('got-newsletter', got_newsletter, name='got-newsletter'),
    path('register', register, name='register'),
    path('signin', signin, name='signin'),
    path('logout/',logout , name='logout'),
    path('book-hotel/<int:pk>', book_hotel, name='book-hotel'),
    path('profile', profile, name='profile'),
   
]
