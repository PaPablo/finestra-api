from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from relat.models import Relat


class RelatTest(APITestCase):

    def test_can_create_relat(self):
        # Given
        data = {'title': "A title"}
        url = reverse('relat-list')

        # When
        response = self.client.post(url, data, format='json')

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Relat.objects.count(), 1)
        self.assertEqual(Relat.objects.get().title, 'A title')

    def test_can_retrieve_relat(self):
        # Given
        r = Relat(title='A title')

        # When
        r.save()

        url = reverse('relat-list')
        response = self.client.get(url, format='json')

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Relat.objects.get().title, 'A title')
