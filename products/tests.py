from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from products.models import Cake, ProductType, Trifle, Marshmallow, Ginger, Cupcake, Product


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

    def test_create_cake(self):
        self.assertIsInstance(self.cake, Cake)

    def test_str_representation(self):
        self.assertEquals(str(self.cake), "test-case-cake")

    def test_saving_and_retrieving_cake(self):
        first_cake = Cake()
        first_cake.product_name = 'test-case-cake-unique'
        first_cake.price = '2999'
        first_cake.product_description = '9.99'
        first_cake.product_ingredients = 'Test text for ingredients'
        first_cake.cake_topping = '[cherry, chocolate, biscuit]'
        first_cake.product_type = ProductType.CAKE
        first_cake.save()

        second_cake = Cake()
        second_cake.product_name = 'test-case-cake-unique-2'
        second_cake.price = '29991'
        second_cake.product_description = '9.99'
        second_cake.product_ingredients = 'Test text for ingredients'
        second_cake.cake_topping = '[cherry, chocolate, biscuit]'
        second_cake.product_type = ProductType.CAKE
        second_cake.save()

        saved_cakes = Cake.objects.all()
        self.assertEqual(saved_cakes.count(), 2)

        first_saved_cake = saved_cakes[saved_cakes.count() - 1]
        second_saved_cake = saved_cakes[saved_cakes.count() - 2]
        self.assertEqual(first_saved_cake.product_name, 'test-case-cake-unique')
        self.assertEqual(second_saved_cake.price, 29991)


class TrifleModelTests(TestCase):
    """Тест модели Trifle"""

    def setUp(self):
        self.trifle = Trifle(
            product_name="test-case-trifle",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            trifle_topping='[cherry, chocolate, biscuit]',
            product_type='TRIFLE',
        )

    def test_create_trifle(self):
        self.assertIsInstance(self.trifle, Trifle)

    def test_str_representation(self):
        self.assertEquals(str(self.trifle), "test-case-trifle")

    def test_saving_and_retrieving_cake(self):
        first_trifle = Trifle()
        first_trifle.product_name = 'test-case-trifle-unique'
        first_trifle.price = '2999'
        first_trifle.product_description = '9.99'
        first_trifle.product_ingredients = 'Test text for ingredients'
        first_trifle.trifle_topping = '[cherry, chocolate, biscuit]'
        first_trifle.product_type = ProductType.TRIFLE
        first_trifle.save()

        second_trifle = Trifle()
        second_trifle.product_name = 'test-case-trifle-unique-2'
        second_trifle.price = '29991'
        second_trifle.product_description = '9.99'
        second_trifle.product_ingredients = 'Test text for ingredients'
        second_trifle.trifle_topping = '[cherry, chocolate, biscuit]'
        second_trifle.product_type = ProductType.TRIFLE
        second_trifle.save()

        saved_trifles = Trifle.objects.all()
        self.assertEqual(saved_trifles.count(), 2)

        first_saved_trifle = saved_trifles[saved_trifles.count() - 1]
        second_saved_trifle = saved_trifles[saved_trifles.count() - 2]
        self.assertEqual(first_saved_trifle.product_name, 'test-case-trifle-unique')
        self.assertEqual(second_saved_trifle.price, 29991)


class MarshmallowModelTests(TestCase):
    """Тест модели Marshmallow"""

    def setUp(self):
        self.marshmallow = Marshmallow(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type='MARSHMALLOW',
        )

    def test_create_marshmallow(self):
        self.assertIsInstance(self.marshmallow, Marshmallow)

    def test_str_representation(self):
        self.assertEquals(str(self.marshmallow), "test-case-marshmallow")

    def test_saving_and_retrieving_cake(self):
        first_marshmallow = Marshmallow()
        first_marshmallow.product_name = 'test-case-marshmallow-unique'
        first_marshmallow.price = '2999'
        first_marshmallow.product_description = '9.99'
        first_marshmallow.product_ingredients = 'Test text for ingredients'
        first_marshmallow.product_type = ProductType.MARSHMALLOW
        first_marshmallow.save()

        second_marshmallow = Marshmallow()
        second_marshmallow.product_name = 'test-case-marshmallow-unique-2'
        second_marshmallow.price = '29991'
        second_marshmallow.product_description = '9.99'
        second_marshmallow.product_ingredients = 'Test text for ingredients'
        second_marshmallow.product_type = ProductType.MARSHMALLOW
        second_marshmallow.save()

        saved_marshmallow = Marshmallow.objects.all()
        self.assertEqual(saved_marshmallow.count(), 2)

        first_saved_marshmallow = saved_marshmallow[saved_marshmallow.count() - 1]
        second_saved_marshmallow = saved_marshmallow[saved_marshmallow.count() - 2]
        self.assertEqual(first_saved_marshmallow.product_name, 'test-case-marshmallow-unique')
        self.assertEqual(second_saved_marshmallow.price, 29991)


class GingerModelTests(TestCase):
    """Тест модели Ginger"""

    def setUp(self):
        self.ginger = Ginger(
            product_name="test-case-ginger",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type='GINGER',
        )

    def test_create_ginger(self):
        self.assertIsInstance(self.ginger, Ginger)

    def test_str_representation(self):
        self.assertEquals(str(self.ginger), "test-case-ginger")

    def test_saving_and_retrieving_cake(self):
        first_ginger = Ginger()
        first_ginger.product_name = 'test-case-ginger-unique'
        first_ginger.price = '2999'
        first_ginger.product_description = '9.99'
        first_ginger.product_ingredients = 'Test text for ingredients'
        first_ginger.product_type = ProductType.GINGER
        first_ginger.save()

        second_ginger = Ginger()
        second_ginger.product_name = 'test-case-ginger-unique-2'
        second_ginger.price = '29991'
        second_ginger.product_description = '9.99'
        second_ginger.product_ingredients = 'Test text for ingredients'
        second_ginger.product_type = ProductType.GINGER
        second_ginger.save()

        saved_ginger = Ginger.objects.all()
        self.assertEqual(saved_ginger.count(), 2)

        first_saved_ginger = saved_ginger[saved_ginger.count() - 1]
        second_saved_ginger = saved_ginger[saved_ginger.count() - 2]
        self.assertEqual(first_saved_ginger.product_name, 'test-case-ginger-unique')
        self.assertEqual(second_saved_ginger.price, 29991)


class CupcakeModelTests(TestCase):
    """Тест модели Cupcake"""

    def setUp(self):
        self.cupcake = Cupcake(
            product_name="test-case-cupcake",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type='CUPCAKE',
        )

    def test_create_cupcake(self):
        self.assertIsInstance(self.cupcake, Cupcake)

    def test_str_representation(self):
        self.assertEquals(str(self.cupcake), "test-case-cupcake")

    def test_saving_and_retrieving_cake(self):
        first_cupcake = Cupcake()
        first_cupcake.product_name = 'test-case-cupcake-unique'
        first_cupcake.price = '2999'
        first_cupcake.product_description = '9.99'
        first_cupcake.product_ingredients = 'Test text for ingredients'
        first_cupcake.product_type = ProductType.CUPCAKE
        first_cupcake.save()

        second_cupcake = Cupcake()
        second_cupcake.product_name = 'test-case-cupcake-unique-2'
        second_cupcake.price = '29991'
        second_cupcake.product_description = '9.99'
        second_cupcake.product_ingredients = 'Test text for ingredients'
        second_cupcake.product_type = ProductType.CUPCAKE
        second_cupcake.save()

        saved_cupcake = Cupcake.objects.all()
        self.assertEqual(saved_cupcake.count(), 2)

        first_saved_cupcake = saved_cupcake[saved_cupcake.count() - 1]
        second_saved_cupcake = saved_cupcake[saved_cupcake.count() - 2]
        self.assertEqual(first_saved_cupcake.product_name, 'test-case-cupcake-unique')
        self.assertEqual(second_saved_cupcake.price, 29991)


class ProductViewTests(TestCase):
    """ Тест для представлений Product"""

    def test_product_list_view(self):
        Marshmallow1 = Product.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
        )

        Marshmallow2 = Product.objects.create(
            product_name="test-case-marshmallow2",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:product-view'))
        self.assertIn('test-case-marshmallow2', response.content.decode())


class CakesViewTests(TestCase):
    """ Тест для представлений Cake"""

    def test_cake_list_view(self):
        Marshmallow1 = Cake.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            cake_topping=" ",
            product_type=ProductType.CAKE,
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:cake-view'))
        self.assertIn('test-case-marshmallow', response.content.decode())


class CupcakesViewTests(TestCase):
    """ Тест для представлений Cake"""

    def test_cupcake_list_view(self):
        Marshmallow1 = Cupcake.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type=ProductType.CUPCAKE,
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:cupcake-view'))
        self.assertIn('test-case-marshmallow', response.content.decode())


class GingerViewTests(TestCase):
    """ Тест для представлений Cake"""

    def test_ginger_list_view(self):
        Marshmallow1 = Ginger.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type=ProductType.GINGER,
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:ginger-view'))
        self.assertIn('test-case-marshmallow', response.content.decode())


class TriflesViewTests(TestCase):
    """ Тест для представлений Cake"""

    def test_trifle_list_view(self):
        Marshmallow1 = Trifle.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type=ProductType.TRIFLE,
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:trifle-view'))
        self.assertIn('test-case-marshmallow', response.content.decode())


class MarshmallowsViewTests(TestCase):
    """ Тест для представлений Cake"""

    def test_marshmallow_list_view(self):
        Marshmallow1 = Marshmallow.objects.create(
            product_name="test-case-marshmallow",
            price='2999',
            product_description='9.99',
            product_ingredients='Test text for ingredients',
            product_type=ProductType.MARSHMALLOW,
        )

        user = User.objects.create_user(username='testuser', password='testpassword')
        user.is_staff = True
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse('products:marshmallow-view'))
        self.assertIn('test-case-marshmallow', response.content.decode())
