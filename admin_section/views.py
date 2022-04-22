from django.shortcuts import render , redirect
from src.models import *
from admin_section.forms import *
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


    
        
  



def ad_logout(request):
    deauth(request)
    messages.success(request , 'Logged out successfully')
    return redirect('signin')

@login_required(login_url='signin')
def dash(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    hts=hotels.objects.all()
    context={
        'hotels':hts
    }
    return render(request, 'employee/dash.html' , context)


@login_required(login_url='signin')
def add_hotel(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    if request.method == 'POST':
        print(request.POST)
        form=HotelForms(request.POST ,request.FILES)
        if form.is_valid():
            print("valid" , form)
            form.save()
            return redirect('dash')

    form = HotelForms()
    context={
        'form':form
    }
    return render(request, 'employee/add_hotel.html' , context)       
@login_required(login_url='signin')
def update_hotel(request , pk):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    hotel=hotels.objects.get(id=pk)
    if request.method == 'POST':
        form=HotelForms(request.POST , request.FILES , instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('dash')
    form = HotelForms(instance=hotel)
    context={
        'form':form
    }
    return render(request, 'employee/add_hotel.html' , context)
@login_required(login_url='signin')
def all_events(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    events=event_type.objects.all()
    context={
        'events':events
    }
    return render(request, 'employee/all_events.html' , context) 
@login_required(login_url='signin')
def add_event(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    if request.method == 'POST':
        form=AddEventForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-events')
    form = AddEventForms()
    context={
        'form':form
    }
    return render(request, 'employee/add_event.html' , context)  


@login_required(login_url='signin')
def update_event(request, pk):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    event=event_type.objects.get(id=pk)
    if request.method == 'POST':
        form=AddEventForms(request.POST , instance=event)
        if form.is_valid():
            form.save()
            return redirect('all-events')
    form = AddEventForms(instance=event)
    context={
        'form':form
    }
    return render(request, 'employee/add_event.html' , context)     

@login_required(login_url='signin')
def all_event_going(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    events=events_going.objects.all()
    context={
        'events':events
    }
    return render(request, 'employee/all_event_going.html' , context)

@login_required(login_url='signin')
def add_events_going_on(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    if request.method == 'POST':
        form=EventGoinOn(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-event-going')
    form = EventGoinOn()
    context={
        'form':form
    }
    return render(request, 'employee/add_event_going.html' , context)
@login_required(login_url='signin')
def update_events_going_on(request, pk):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    event=events_going.objects.get(id=pk)
    if request.method == 'POST':
        form=EventGoinOn(request.POST , request.FILES , instance=event)
        if form.is_valid():
            form.save()
            return redirect('all-event-going')
    form = EventGoinOn(instance=event)
    context={
        'form':form
    }
    return render(request, 'employee/add_event_going.html' , context)
@login_required(login_url='signin')
def all_newsletter(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    newsletters=newsletter.objects.all()
    context={
        'newsletters':newsletters
    }
    return render(request, 'employee/all_newsletter.html' , context)
@login_required(login_url='signin')
def  all_booking_hotel(request):
    if not request.user.is_superuser:
        messages.success(request , 'You are not authorized to view this page')
        return redirect('home')
    bookings=booking_hotel.objects.all().order_by("-id")
    context={
        'bookings':bookings
    }
    return render(request, 'employee/all_booking_hotel.html' , context)
