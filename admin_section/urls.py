from django.urls import path
from .views import *



urlpatterns = [
    
    path('dash/' , dash , name="dash"),
    path('add-hotel/' , add_hotel , name="add-hotel"),
    path('update-hotel/<int:pk>' , update_hotel , name="update-hotel"),
    path('all-events/' , all_events , name="all-events"),
    path('add-event/' , add_event , name="add-event"),
    path('update-event/<int:pk>/' , update_event , name="update-event"),
    path('all-event-going' , all_event_going , name="all-event-going"),
    path('add-events-going-on/' , add_events_going_on , name="add-events-going-on"),
    path('update-events-going-on/<int:pk>/' , update_events_going_on , name="update-events-going-on"),
    path('all-newsletter/' , all_newsletter , name="all-newsletter"),
    path('all_booking_hotel/' , all_booking_hotel , name="all_booking_hotel"),
    path('ad-logout', ad_logout , name="ad-logout"),
   
]
