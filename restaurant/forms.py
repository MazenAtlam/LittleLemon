"""
This module contains the form definitions for the restaurant booking system.
"""

from django.forms import ModelForm
from .models import Booking


# pylint: disable=too-few-public-methods
class BookingForm(ModelForm):
    """A form for creating and updating Booking instances.
    This form is automatically generated from the Booking model and includes
    all fields from the model.

    Attributes:
        Meta (class): A nested class that specifies the model and fields to be used
                      in the form.
    """

    class Meta:
        """A class that specifies the model and fields to be used in the form.
        Attributes:
            model (Booking): The model to be used in the form.
            fields (list): The fields from the model to be included in the form.
        """

        model = Booking
        fields = "__all__"
