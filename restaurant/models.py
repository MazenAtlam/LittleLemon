"""
This module defines the models for the restaurant application.
"""

from django.db import models


class Booking(models.Model):
    """
    Booking model represents a reservation made by a customer.

    Attributes:
        name (CharField): The name of the customer making the reservation.
            Maximum length is 200 characters.
        reservation_date (DateField): The date of the reservation.
        reservation_slot (SmallIntegerField): The time slot for the reservation.
            Default value is 10.

    Methods:
        __str__(): Returns the name of the customer.
    """

    name = models.CharField(max_length=200)
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField()

    def __str__(self):
        """
        A string representation of the object

        Returns:
            str: The first name of the object.
        """

        return str(self.name)


class Menu(models.Model):
    """A Django model representing a menu item in a restaurant.

    Attributes:
        name (CharField): The name of the menu item, with a maximum length of 200 characters.
        price (IntegerField): The price of the menu item, which cannot be null.
        menu_item_description (TextField): A description of the menu item,
            with a maximum length of 1000 characters.
        Category (ForeignKey): A foreign key to the Category model,
            with a cascade delete option and a related name 'menu_items'.

    Methods:
        __str__(): Returns the name of the menu item as its string representation.
    """

    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default="")
    Category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="menu_items", default=0
    )

    def __str__(self):
        """
        A string representation of the object

        Returns:
            str: The first name of the object.
        """

        return str(self.name)


class Category(models.Model):
    """Category model to represent different categories in the restaurant.

    Attributes:
        name (str): The name of the category.
            It must be unique and can have a maximum length of 50 characters.

    Methods:
        __str__(): Returns the name of the category as its string representation.
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        A string representation of the object

        Returns:
            str: The first name of the object.
        """

        return str(self.name)
