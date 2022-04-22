from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class hotels(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.name

class event_type(models.Model):
    event= models.CharField(max_length=100)

    def __str__(self):
        return self.event

class booking_hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(hotels, on_delete=models.CASCADE)
    event_type_id = models.ForeignKey(event_type, on_delete=models.CASCADE)
    event_description = models.TextField()
    check_in = models.DateField()
    event_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)





class newsletter(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class events_going(models.Model):
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='event_images')

    def __str__(self):
        return self.event_name

    
