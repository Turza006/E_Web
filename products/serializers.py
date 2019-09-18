from rest_framework import serializers
from .models import Catagory,Products

class CatagorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = ['name']


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('name','detail','url','catagorys','seller')