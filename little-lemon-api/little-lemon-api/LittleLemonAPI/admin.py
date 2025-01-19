from django.contrib import admin

from . import models


# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "featured", "category"]
    list_filter = ["category"]
    search_fields = ["title"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    search_fields = ["title"]

admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
