import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


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
    price = models.IntegerField(null=False, blank=True)
    product_image = models.ImageField(default='default-product.png', upload_to=path_to_rename)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.product_name}"

