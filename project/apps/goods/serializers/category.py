from rest_framework import serializers

from apps.goods.models import Category
from .property import PropertyObjectRetrieveSerializer


class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
        read_only_fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    properties = PropertyObjectRetrieveSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'properties', 'created_at', 'updated_at')
        read_only_fields = ('id', 'title', 'slug', 'properties', 'created_at', 'updated_at')
