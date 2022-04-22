from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



class HotelForm(forms.ModelForm):
    event_type_id = forms.ModelChoiceField(queryset=event_type.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    event_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    check_in = forms.DateField(label="Select Check-In Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))   
    event_date = forms.DateField(label="Select Event Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
        
    class Meta:
        model = booking_hotel
        exclude = ['user','hotel_id']
        