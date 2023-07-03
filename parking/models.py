from django.db import models

from authentication.models import CustomUser


class ParkingSpot(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField()
    reservation_time = models.DateTimeField(auto_now_add=True)
    reservation_end_time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"Reservation {self.pk}"
