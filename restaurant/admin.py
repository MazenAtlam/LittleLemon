"""
This module registers the models with the Django admin site.
"""

from django.contrib import admin
from .models import Menu
from .models import Category


admin.site.register(Menu)
admin.site.register(Category)
