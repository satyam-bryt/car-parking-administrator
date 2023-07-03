from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ParkingSpotListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_parking_spots(self):
        url = reverse('parking:parking-spot-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "parking_spots")
        self.assertContains(response, "reserved_spots")

    def test_post_nearby_parking_spots(self):
        url = reverse('parking-spot-list')
        data = {
            'latitude': '12.3456',
            'longitude': '78.9101',
            'distance': '10.0',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "parking_spots")
        self.assertContains(response, "reserved_spots")

    def test_post_invalid_data(self):
        url = reverse('parking-spot-list')
        data = {
            'latitude': 'invalid_latitude',
            'longitude': 'invalid_longitude',
            'distance': 'invalid_distance',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
