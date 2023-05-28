from django.test import TestCase
from product.models import *

class BrandTestCase(TestCase):
    def setUp(self):
        Brand.objects.create(name="BMW")

    def test_if_we_can_create_brand(self):
        """Animals that can speak are correctly identified"""
        car = Brand.objects.get(name="BMW")
        self.assertEqual(car.name, 'BMW')