"""
This module contains the configuration for the 'restaurant' application.
"""

from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """
    Configuration class for the 'restaurant' application.

    This class inherits from Django's AppConfig and is used to configure
    the 'restaurant' application. It sets the default auto field type to
    'BigAutoField' and specifies the name of the application as 'restaurant'.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant"
