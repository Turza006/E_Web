from rest_framework import serializers
from .models import Catagory,Products
from rest_framework import permissions

class CatagorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = ['name']
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('name','detail','url','catagorys','seller')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)