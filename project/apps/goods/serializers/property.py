from rest_framework import serializers

from apps.goods.models import PropertyObject, PropertyValue


class PropertyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyObject
        fields = ('id', 'code', 'created_at', 'updated_at')
        read_only_fields = ('id', 'code', 'created_at', 'updated_at')


class PropertyValueSerializer(serializers.ModelSerializer):
    property_obj = PropertyObjectSerializer()

    class Meta:
        model = PropertyValue
        fields = ('id', 'type_str', 'type_number', 'code', 'property_obj')
        read_only_fields = ('id', 'type_str', 'type_number', 'code', 'property_obj')


class PropertyValueRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValue
        fields = ('id', 'type_str', 'type_number', 'code')
        read_only_fields = ('id', 'type_str', 'type_number', 'code')


class PropertyObjectRetrieveSerializer(serializers.ModelSerializer):
    property_value = PropertyValueRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = PropertyObject
        fields = ('id', 'code', 'property_value', 'created_at', 'updated_at')
        read_only_fields = ('id', 'code', 'property_value', 'created_at', 'updated_at')
