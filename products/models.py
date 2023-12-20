import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
import json


def path_to_rename(instance, filename):
    upload_to = 'product_images'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}_{}.{}'.format(instance.pk, instance.product_name, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Product(models.Model):
    product_name = models.CharField(null=False, blank=False, max_length=100)
    price = models.IntegerField(null=True, blank=True)
    product_image = models.ImageField(default='default-product.png', upload_to=path_to_rename)
    product_description = models.TextField(null=True, blank=True)
    product_ingredients = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.product_name}"


class Cake(Product):
    cake_topping = models.CharField()

    def set_topping(self, x):
        self.cake_topping = json.dumps(x)

    def get_topping(self):
        return json.loads(self.cake_topping)

    class Meta:
        verbose_name = _("cake")
        verbose_name_plural = _("cakes")
        ordering = ["-id"]


class Trifle(Product):
    trifle_topping = models.CharField()

    def set_topping(self, x):
        self.trifle_topping = json.dumps(x)

    def get_topping(self):
        return json.loads(self.trifle_topping)

    class Meta:
        verbose_name = _("trifle")
        verbose_name_plural = _("trifles")
        ordering = ["-id"]


class Marshmallow(Product):
    class Meta:
        verbose_name = _("marshmallow")
        verbose_name_plural = _("marshmallows")
        ordering = ["-id"]


class Ginger(Product):
    class Meta:
        verbose_name = _("ginger")
        verbose_name_plural = _("gingers")
        ordering = ["-id"]


class Cupcake(Product):
    class Meta:
        verbose_name = _("cupcake")
        verbose_name_plural = _("cupcakes")
        ordering = ["-id"]
