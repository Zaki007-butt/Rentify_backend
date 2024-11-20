from rest_framework import serializers
from .models import Property, PropertyCategory, PropertyType, Agreement, Customer
from account.models import User

class PropertySerializer(serializers.ModelSerializer):
  property_category_name = serializers.SerializerMethodField()
  property_type_name = serializers.SerializerMethodField()

  class Meta:
    model = Property
    fields = [
      'id', 'title', 'description', 'price', 'address', 'city', 'status', 'rent_or_buy',
      'bedroom', 'washroom', 'area', 'property_category', 'property_type',
      'property_category_name', 'property_type_name', 'created_at', 'updated_at'
    ]

  def get_property_category_name(self, obj):
    return obj.property_category.name if obj.property_category else None

  def get_property_type_name(self, obj):
    return obj.property_type.name if obj.property_type else None


class PropertyCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyCategory
    fields = '__all__'

class PropertyTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyType
    fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
  user = serializers.SerializerMethodField(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user',
    write_only=True
  )

  class Meta:
    model = Customer
    fields = '__all__'

  def get_user(self, obj):
    user = obj.user
    return {
      'id': user.id,
      'email': user.email,
      'name': user.name
    }

class AgreementSerializer(serializers.ModelSerializer):
  # Nested serializers for related fields
  property = PropertySerializer(read_only=True)
  property_id = serializers.PrimaryKeyRelatedField(
    queryset=Property.objects.all(),
    source='property',
    write_only=True
  )

  customer = CustomerSerializer(read_only=True)
  customer_id = serializers.PrimaryKeyRelatedField(
    queryset=Customer.objects.all(),
    source='customer',
    write_only=True
  )

  class Meta:
    model = Agreement
    fields = '__all__'

  def get_customer(self, obj):
    customer = obj.customer
    return {
      'id': customer.id,
      'cnic': customer.cnic,
      'phone_number': customer.phone_number,
      'address': customer.address
    }