from django.shortcuts import render , redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# Project 3
# Hotel Listing

# Admin panel:
# Can see the all the user, add,delete and update user.

# Hotel dashboard
# *Can list their hotels on the portal
# * Hotel details

# User dashboard
# *Can see all the listed hotels on the homepage
# *Book the hotels for particular events
# * Various events going on in the hotels.


def home(request):
    hots=hotels.objects.all().order_by("-id")
    events=events_going.objects.all()
    context={
        'hotels':hots,
        'events':events
    }
    return render(request, 'home.html' , context)


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')

    else:
        f = UserCreationForm()

    return render(request, 'register.html', {'form': f})
def logout(request):
    deauth(request)
    messages.success(request , 'Logged out successfully')
    return redirect('home')


def got_newsletter(request):
    if request.method=='POST':
        em= request.POST.get('email')
        newsletter.objects.create(email=em)
        messages.success(request, 'Thank you for subscribing to our newsletter')
        return redirect('home')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username , password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect('dash')
            else:    
                login(request , user)
                messages.success(request , 'Logged in successfully')
                return redirect('home')
        else:
            messages.error(request , 'Invalid username or password')
            return redirect('signin')
    return render(request,'signin.html')

@login_required(login_url='signin')
def book_hotel(request , pk):
    get_book = hotels.objects.get(id=pk)
   
    if request.method=='POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.user = request.user
            fr.hotel_id = get_book
            fr.save()
            messages.success(request , 'Booking successful | will call you as soon as possible')
            return redirect('home')    
    context={
        'book':get_book,
        'form':HotelForm()
    }
    return render(request , 'book.html' , context)

@login_required(login_url='signin')
def profile(request):
    get_prof=booking_hotel.objects.filter(user=request.user)
    context={
        'bookings':get_prof
    }
    return render(request , 'profile.html' , context)
