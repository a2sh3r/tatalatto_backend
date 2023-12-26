from django.shortcuts import render
from rest_framework import generics

# Create your views here.

# TODO create views for Product
from rest_framework.permissions import IsAdminUser

from products.models import Product, Cake, Cupcake, Ginger, Trifle, Marshmallow
from products.serializers import ProductsSerializer, CakeSerializer, CupcakeSerializer, GingerSerializer, \
    TrifleSerializer, MarshmallowSerializer


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminUser]


class CakesListView(generics.ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [IsAdminUser]


class CakesDetailView(generics.RetrieveAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [IsAdminUser]


class CupcakesListView(generics.ListAPIView):
    queryset = Cupcake.objects.all()
    serializer_class = CupcakeSerializer
    permission_classes = [IsAdminUser]


class CupcakesDetailView(generics.RetrieveAPIView):
    queryset = Cupcake.objects.all()
    serializer_class = CupcakeSerializer
    permission_classes = [IsAdminUser]


class GingersListView(generics.ListAPIView):
    queryset = Ginger.objects.all()
    serializer_class = GingerSerializer
    permission_classes = [IsAdminUser]


class GingersDetailView(generics.RetrieveAPIView):
    queryset = Ginger.objects.all()
    serializer_class = GingerSerializer
    permission_classes = [IsAdminUser]


class TriflesListView(generics.ListAPIView):
    queryset = Trifle.objects.all()
    serializer_class = TrifleSerializer
    permission_classes = [IsAdminUser]


class TriflesDetailView(generics.RetrieveAPIView):
    queryset = Trifle.objects.all()
    serializer_class = TrifleSerializer
    permission_classes = [IsAdminUser]


class MarshmallowsListView(generics.ListAPIView):
    queryset = Marshmallow.objects.all()
    serializer_class = MarshmallowSerializer
    permission_classes = [IsAdminUser]


class MarshmallowsDetailView(generics.RetrieveAPIView):
    queryset = Marshmallow.objects.all()
    serializer_class = MarshmallowSerializer
    permission_classes = [IsAdminUser]
