from django.utils import timezone
from rest_framework import serializers

from parking.models import ParkingSpot, Reservation


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ('id', 'name', 'latitude', 'longitude')


class ReservationSerializer(serializers.ModelSerializer):
    parking_spot = ParkingSpotSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('id', 'user', 'parking_spot', 'hours', 'reservation_time', 'reservation_end_time', 'status')

    def get_status(self, obj):
        if obj.reservation_end_time >= timezone.now():
            return 'Active'
        else:
            return 'Inactive'
