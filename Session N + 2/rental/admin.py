from django.contrib import admin
from rental.models import Rental, Inventory

# Register your models here.

admin.site.register(Rental)
admin.site.register(Inventory)