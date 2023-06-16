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
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    # class Meta:
    #     model = Product
    #     fields = ['id', 'title', 'unit_price', 'collection']
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(
        method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail',
    )

    def calculate_tax(self, product):
        request = self.context.get('request')
        return product.unit_price * Decimal(1.1)
