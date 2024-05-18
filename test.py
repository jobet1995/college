from django.test import TestCase, Client
from django.urls import reverse


class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_view(self):
        response = self.client.get(reverse('my-view'))
        self.assertEqual(response.status_code, 200)
