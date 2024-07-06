from django.contrib import admin
from .models import Property, PropertyCategory, PropertyType

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
