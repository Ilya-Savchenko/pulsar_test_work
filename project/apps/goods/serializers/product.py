from rest_framework import serializers

from apps.goods.models import Product, Category, PropertyValue
from apps.goods.serializers.category import CategoryShortSerializer
from apps.goods.serializers.property import PropertyValueSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    property_values = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=PropertyValue.objects.all(),
        required=False
    )

    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'category', 'property_values')
        read_only_fields = ('id',)


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryShortSerializer()

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'sku', 'category', 'created_at', 'updated_at')
        read_only_fields = ('id', 'title', 'slug', 'sku', 'category', 'created_at', 'updated_at')


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryShortSerializer()
    property_values = PropertyValueSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'sku', 'category', 'property_values', 'created_at', 'updated_at')
        read_only_fields = ('id', 'title', 'slug', 'sku', 'category', 'property_values', 'created_at', 'updated_at')


class ProductUpdateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    property_values = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=PropertyValue.objects.all(),
        required=False
    )

    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'category', 'slug', 'property_values', 'created_at', 'updated_at')
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')
