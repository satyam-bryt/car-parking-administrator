import json

from datetime import timedelta

from django.utils import timezone
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from parking.api_utils import calculate_distance
from parking.models import ParkingSpot, Reservation
from parking.serializers import ParkingSpotSerializer, ReservationSerializer


@permission_classes([AllowAny])
class ParkingSpotList(APIView):
    def get(self, request):
        reserved_spots = list(Reservation.objects.filter(reservation_end_time__gte=timezone.now())
                                                 .values_list('parking_spot_id', flat=True))
        parking_spots = ParkingSpot.objects.all()
        serializer = ParkingSpotSerializer(parking_spots, many=True)
        return HttpResponse(json.dumps({"parking_spots": serializer.data,
                                        "reserved_spots": reserved_spots}),
                            content_type='application/json',
                            status=status.HTTP_200_OK)

    def post(self, request):

        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        distance = request.POST.get('distance')

        latitude = float(latitude)
        longitude = float(longitude)
        distance = float(distance)

        parking_spots = ParkingSpot.objects.all()
        nearby_parking_spots = []

        for spot in parking_spots:
            spot_latitude = spot.latitude
            spot_longitude = spot.longitude
            computed_distance = calculate_distance(latitude, longitude, spot_latitude, spot_longitude)

            if computed_distance <= distance:
                nearby_parking_spots.append(spot)
        serializer = ParkingSpotSerializer(nearby_parking_spots, many=True)
        reserved_spots = list(Reservation.objects.filter(reservation_end_time__gte=timezone.now())
                              .values_list('parking_spot_id', flat=True))

        return HttpResponse(json.dumps({"parking_spots": serializer.data,
                                        "reserved_spots": reserved_spots}),
                            content_type='application/json',
                            status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class ReserveParkingSpot(APIView):
    def post(self, request):
        parking_spot_id = request.POST.get('id')
        user_id = request.POST.get('user')
        hours = request.POST.get('hours')

        Reservation.objects.create(parking_spot_id=parking_spot_id,
                                   user_id=user_id,
                                   hours=hours,
                                   reservation_end_time=timezone.now() + timedelta(hours=int(hours)))

        return HttpResponse(json.dumps({"message": "success"}),
                            content_type='application/json',
                            status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class ExistingReservations(APIView):
    def get(self, request, user_id):
        all_reservations = Reservation.objects.filter(user_id=user_id)
        serializer = ReservationSerializer(all_reservations, many=True)
        return HttpResponse(json.dumps({"all_reserved_spots": serializer.data}),
                            content_type='application/json',
                            status=status.HTTP_200_OK)
