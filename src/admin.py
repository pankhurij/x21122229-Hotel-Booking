from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(hotels)
class hotelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'description', 'image1', )
    search_fields = ('name', 'location', 'price', 'description', 'image1', )
    list_per_page = 25

@admin.register(event_type)
class event_typeAdmin(admin.ModelAdmin):
    list_display = ('event',)
    search_fields = ('event',)
    list_per_page = 25


@admin.register(booking_hotel)
class booking_hotelAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel_id', 'event_type_id', 'event_description', 'check_in', 'event_date', 'booking_date')
    search_fields = ('user', 'hotel_id', 'event_type_id', 'event_description', 'check_in', 'event_date', 'booking_date')
    list_per_page = 25


@admin.register(newsletter)
class newsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ('email', 'date')
    list_per_page = 25


@admin.register(events_going)
class events_goingAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_location', 'event_image')
    search_fields = ('event_name', 'event_location', 'event_image')
    list_per_page = 25
