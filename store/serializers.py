from rest_framework import serializers
from decimal import Decimal
from .models import Collection

from store.models import Product

# https://www.django-rest-framework.org/

# SERIALIZING RELATIONSHIPS methods:
# primary key
# string
# Nested object
# hyperlink


class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name="calculate_tax")

    def calculate_tax(self, product):
        request = self.context.get('request')
        return product.unit_price * Decimal(1.1)

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance
