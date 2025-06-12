from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ProductTests(TestCase):
    def test_product_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['products']), 2)