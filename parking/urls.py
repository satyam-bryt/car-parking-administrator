from django.urls import path

from parking.apis import *
from parking.views import *

app_name = 'parking'

urlpatterns = [
    path('', CarParkingAdministrator.as_view(), name='base'),
    path('existing/reservations', ExistingReservationsView.as_view(), name='existing-reservations'),
    path('spots/list', ParkingSpotList.as_view(), name='parking-spot-list'),
    path('reserve/spot', ReserveParkingSpot.as_view(), name='reserve-parking-spot'),
    path('reserved/spots/list/<int:user_id>', ExistingReservations.as_view(), name='reserved-spots-list'),
]
