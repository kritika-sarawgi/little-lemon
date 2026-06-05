from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Menu, Booking


class MenuAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.token = Token.objects.create(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

    def test_create_menu_item(self):

        data = {
            'title': 'Pasta',
            'price': '15.99',
            'inventory': 25
        }

        response = self.client.post(
            '/restaurant/menu/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_menu_items(self):

        Menu.objects.create(
            title='Pizza',
            price=10.99,
            inventory=20
        )

        response = self.client.get(
            '/restaurant/menu/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class BookingAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='bookinguser',
            password='bookingpass123'
        )

        self.token = Token.objects.create(
            user=self.user
        )

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

    def test_create_booking(self):

        data = {
            'name': 'John Doe',
            'no_of_guests': 4,
            'booking_date': '2026-06-15'
        }

        response = self.client.post(
            '/restaurant/booking/tables/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_bookings(self):

        Booking.objects.create(
            name='Jane Doe',
            no_of_guests=2,
            booking_date='2026-06-15'
        )

        response = self.client.get(
            '/restaurant/booking/tables/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class HomePageTest(APITestCase):

    def test_home_page(self):

        response = self.client.get('/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )