from rest_framework import serializers
from .models import Property

# class PropertySerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Property
#     fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
  property_category_name = serializers.SerializerMethodField()
  property_type_name = serializers.SerializerMethodField()

  class Meta:
    model = Property
    fields = [
      'id', 'title', 'description', 'price', 'address', 'status',
      'bedroom', 'washroom', 'area', 'property_category', 'property_type',
      'property_category_name', 'property_type_name', 'created_at', 'updated_at'
    ]

  def get_property_category_name(self, obj):
    return obj.property_category.name if obj.property_category else None

  def get_property_type_name(self, obj):
    return obj.property_type.name if obj.property_type else None