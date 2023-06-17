from rest_framework import serializers
from decimal import Decimal
from .models import Collection
from django.db.models.aggregates import Count
from store.models import Product

# https://www.django-rest-framework.org/

# SERIALIZING RELATIONSHIPS methods:
# primary key
# string
# Nested object
# hyperlink


class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()

    # product_count = serializers.SerializerMethodField(method_name="get_count")

    # def get_count(self, collection):
    #     queryset = Product.objects.filter(collection=collection.id).count()
    #     return queryset


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
