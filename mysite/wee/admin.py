from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Washroom, Review

# Register your models here.

@admin.register(Washroom)
class WeeAdmin(OSMGeoAdmin):
    list_display = ('name', 'rating','disable_access','unisex','location')

