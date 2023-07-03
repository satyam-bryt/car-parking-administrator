from django.core.management.base import BaseCommand
from parking.models import *
from faker import Faker
from django.db import models

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 101):
            parking_spot = ParkingSpot(name=f"P{i}",
                                       latitude=fake.latitude(),
                                       longitude=fake.longitude())
            parking_spot.save()

