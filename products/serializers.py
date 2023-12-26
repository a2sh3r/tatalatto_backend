from rest_framework import serializers

from products.models import Product, Cake, Marshmallow, Trifle, Ginger, Cupcake


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = "__all__"


class CupcakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupcake
        fields = "__all__"


class GingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ginger
        fields = "__all__"


class TrifleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trifle
        fields = "__all__"


class MarshmallowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marshmallow
        fields = "__all__"