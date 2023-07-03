from django.contrib import admin

# Register your models here.
from parking.models import *

admin.site.register(CustomUser)
admin.site.register(ParkingSpot)
admin.site.register(Reservation)
