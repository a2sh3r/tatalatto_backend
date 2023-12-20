from django.test import TestCase

from products.models import Cake


class CakeModelTests(TestCase):
    """Тест модели Cake"""

    def setUp(self):
        self.cake = Cake(
            product_name='test-case-cake',
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            cake_topping='[cherry, chocolate, biscuit]',
            product_type='CAKE',
        )

    def test_create_book(self):
        self.assertIsInstance(self.cake, Cake)

    def test_str_representation(self):
        self.assertEquals(str(self.cake), "test-case-cake")
