"""
This module registers the models with the Django admin site.
"""

from django.contrib import admin
from .models import Menu
from .models import Category
from .models import Booking


admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Category)
