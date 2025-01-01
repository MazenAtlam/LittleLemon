"""
Views for the Little Lemon restaurant application.

This module contains view functions for rendering HTML templates and handling
HTTP requests related to the restaurant's menu, reservations, and bookings.
"""

from datetime import datetime
import json
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import BookingForm
from .models import Menu
from .models import Booking


# pylint: disable=E1101
def home(request):
    """
    Renders the home page of the restaurant website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """

    return render(request, "index.html")


def about(request):
    """
    Handles the HTTP request for the 'About' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about.html' template.
    """

    return render(request, "about.html")


def reservations(request):
    """
    Handles the reservations view for the restaurant.

    This function retrieves the date from the GET request parameters or defaults
    to the current date if not provided. It then fetches all booking records from
    the database, serializes them into JSON format, and renders the 'bookings.html'
    template with the serialized bookings data.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about
                               the request.

    Returns:
        HttpResponse: The rendered 'bookings.html' template with the bookings data
                      in JSON format.
    """

    # date = request.GET.get('date', datetime.today().date())
    booking_objects = Booking.objects.all()
    booking_json = serializers.serialize("json", booking_objects)
    return render(request, "bookings.html", {"bookings": booking_json})


def book(request):
    """
    Handle the booking form submission and rendering.

    This view function handles both GET and POST requests for the booking form.
    On a GET request, it initializes an empty BookingForm and renders the 'book.html' template.
    On a POST request, it populates the BookingForm with the submitted data, validates it,
    and saves it if the data is valid.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'book.html' template with the form context.
    """

    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


# Add your code here to create new views


def menu(request):
    """
    Handles the request to display the menu.

    This view function retrieves all menu items from the Menu model,
    organizes them into a dictionary, and renders the 'menu.html' template
    with the menu data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'menu.html' template with the menu data.
    """

    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, primary_key=None):
    """
    View function to display a menu item.
    Args:
        request (HttpRequest): The HTTP request object.
        primary_key (int, optional): The primary key of the menu item to display. Defaults to None.
    Returns:
        HttpResponse: The rendered HTML page displaying the menu item.
    """

    if primary_key:
        menu_item = Menu.objects.get(primary_key=primary_key)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


@csrf_exempt
def bookings(request):
    """
    Handle booking requests for the restaurant.

    If the request method is POST, it attempts to create a new booking with the provided data.
    If a booking with the same reservation date and slot already exists,
    it returns an error response. Otherwise, it saves the new booking.

    If the request method is GET, it retrieves all bookings for the specified date
    (or today's date if not specified) and returns them in JSON format.

    Args:
        request (HttpRequest): The HTTP request object containing method, GET, and POST data.

    Returns:
        HttpResponse: A JSON response containing booking data or an error message.
    """

    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if not exist:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())

    today_bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", today_bookings)

    return HttpResponse(booking_json, content_type="application/json")
