from django import forms


class HotelForms(forms.ModelForm):
    class Meta:
        model = hotels
        fields = '__all__'


class AddEventForms(forms.ModelForm):
    class Meta:
        model = event_type
        fields = '__all__'

class EventGoinOn(forms.ModelForm):
    class Meta:
        model = events_going
        fields = '__all__'
