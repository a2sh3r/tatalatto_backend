from django.shortcuts import render
from rest_framework import generics

# Create your views here.

#TODO create views for Product
from rest_framework.permissions import IsAdminUser

from products.models import Product
from products.serializers import ProductsSerializer


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminUser]
