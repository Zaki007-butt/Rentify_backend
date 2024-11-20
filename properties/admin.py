from django.contrib import admin
from .models import Property, PropertyCategory, PropertyType, Customer, Agreement

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
  list_display = ('title', 'price', 'address', 'status', 'property_category', 'property_type', 'created_at', 'updated_at')
  list_filter = ('status', 'property_category', 'property_type')
  search_fields = ('title', 'address', 'description')

@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
  list_display = ('name', 'category')
  list_filter = ('category',)
  search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ('user', 'cnic', 'phone_number', 'address')
  search_fields = ('cnic', 'phone_number', 'address')

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
  list_display = ('property', 'customer', 'status', 'created_at')
  list_filter = ('status', 'property')
  search_fields = ('property__title', 'customer__cnic')
