from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_datetime, parse_date
from django.utils.timezone import make_aware

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        reservation_date = parse_datetime(data['reservation_date'])
        if reservation_date is None:
            return JsonResponse({"error": "Invalid date format"}, status=400)
        if reservation_date.tzinfo is None:
            reservation_date = make_aware(reservation_date)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).exists()
        if exist == False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=reservation_date,
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return JsonResponse({"error": "Booking already exists for this date"}, status=400)

    date_str = request.GET.get('date', datetime.today().date().isoformat())
    date = parse_date(date_str)

    bookings = Booking.objects.all().filter(reservation_date__date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
