"""
URL configuration for the restaurant app.

This module defines the URL patterns for the restaurant application. It maps
URLs to their corresponding view functions in the views module.

Available URL patterns:
- '' : Home page
- 'about/' : About page
- 'book/' : Booking page
- 'reservations/' : Reservations page
- 'menu/' : Menu page
- 'menu_item/<int:primary_key>/' : Display specific menu item by primary key
- 'bookings' : Bookings page

Each URL pattern is associated with a view function and a name for easy reference.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:primary_key>/", views.display_menu_item, name="menu_item"),
    path("bookings", views.bookings, name="bookings"),
]
