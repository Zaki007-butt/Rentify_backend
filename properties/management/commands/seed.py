from django.core.management.base import BaseCommand
from properties.models import PropertyCategory, PropertyType, Property
import random

class Command(BaseCommand):
  help = 'Seed the database with initial data'

  def handle(self, *args, **kwargs):
    self.stdout.write('Seeding database...')
    self.create_categories_and_types()
    self.create_properties()
    self.stdout.write('Database seeding completed.')

  def create_categories_and_types(self):
    categories_and_types = {
      'Residential': ['Apartment', 'House', 'Villa'],
      'Commercial': ['Office', 'Shop', 'Warehouse'],
      'Land': ['Plot', 'Agricultural Land', 'Industrial Land']
    }

    self.categories = []
    self.types = []

    for category_name, type_names in categories_and_types.items():
      category = PropertyCategory.objects.create(name=category_name)
      self.categories.append(category)
      for type_name in type_names:
        property_type = PropertyType.objects.create(name=type_name, category=category)
        self.types.append(property_type)

  def create_properties(self):
    titles = [
      'Beautiful Apartment in the City Center', 'Cozy House in the Suburbs', 'Luxury Villa by the Beach',
      'Modern Office Space', 'Spacious Shop in Downtown', 'Large Warehouse',
      'Prime Plot of Land', 'Fertile Agricultural Land', 'Industrial Land for Development'
    ]

    descriptions = [
      'A beautiful place to live.', 'A cozy home for a family.', 'A luxurious villa with sea views.',
      'A modern office space for your business.', 'A spacious shop in a prime location.', 'A large warehouse for storage.',
      'A prime plot of land for development.', 'Fertile land for farming.', 'Industrial land for business expansion.'
    ]

    prices = [150000.00, 200000.00, 250000.00, 300000.00, 350000.00, 400000.00, 450000.00, 500000.00, 550000.00]
    addresses = [
      '123 Main St', '456 Oak St', '789 Pine St', '101 Maple Ave', '202 Birch Ave', '303 Cedar Ave',
      '404 Elm St', '505 Ash St', '606 Willow St'
    ]

    for i in range(len(titles)):
      Property.objects.create(
        title=titles[i],
        description=descriptions[i],
        price=prices[i],
        address=addresses[i],
        status=random.choice(['active', 'inactive']),
        property_category=random.choice(self.categories),
        property_type=random.choice(self.types)
      )
