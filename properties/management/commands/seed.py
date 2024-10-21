from django.core.management.base import BaseCommand
from properties.models import PropertyCategory, PropertyType, Property
import random

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")
        self.create_categories_and_types()
        self.create_properties()
        self.stdout.write("Database seeding completed.")

    def create_categories_and_types(self):
        categories_and_types = {
            "Residential": ["Apartment", "House", "Villa"],
            "Commercial": ["Office", "Shop", "Warehouse"],
            "Land": ["Plot", "Agricultural Land", "Industrial Land"],
        }

        self.categories = []
        self.types = []

        for category_name, type_names in categories_and_types.items():
            category, _ = PropertyCategory.objects.get_or_create(name=category_name)
            self.categories.append(category)
            for type_name in type_names:
                property_type, _ = PropertyType.objects.get_or_create(
                    name=type_name, category=category
                )
                self.types.append(property_type)

    def create_properties(self):
        titles = [
            "Spacious Apartment in Downtown",
            "Modern House with Garden View",
            "Luxury Villa near the Lake",
            "Central Office Space with City View",
            "Prime Location Shop for Rent",
            "Large Warehouse for Storage",
            "Scenic Plot of Land with Mountain Views",
            "Fertile Agricultural Land for Sale",
            "Industrial Land for Development",
        ]

        descriptions = [
            "A spacious and modern apartment located in the heart of the city.",
            "A cozy house with a beautiful garden, perfect for a family.",
            "A luxurious villa offering stunning views of the nearby lake.",
            "Modern office space strategically located with panoramic city views.",
            "Prime retail space in a bustling commercial area, ideal for businesses.",
            "Large warehouse facility suitable for various storage needs.",
            "Scenic plot of land offering breathtaking mountain views, ideal for a vacation home.",
            "Fertile agricultural land suitable for farming and cultivation.",
            "Industrial land strategically positioned for business expansion and development.",
        ]

        prices = [
            150000.00,
            200000.00,
            250000.00,
            300000.00,
            350000.00,
            400000.00,
            450000.00,
            500000.00,
            550000.00,
        ]
        addresses = [
            "123 Main St",
            "456 Oak St",
            "789 Pine St",
            "101 Maple Ave",
            "202 Birch Ave",
            "303 Cedar Ave",
            "404 Elm St",
            "505 Ash St",
            "606 Willow St",
        ]

        # Ensure there are categories and types created before creating properties
        if not PropertyCategory.objects.exists() or not PropertyType.objects.exists():
            self.stdout.write(
                self.style.ERROR("No property categories or types available.")
            )
            return

        for _ in range(200):
            Property.objects.create(
                title=random.choice(titles),
                description=random.choice(descriptions),
                price=random.choice(prices),
                address=random.choice(addresses),
                status=random.choice(["active", "inactive"]),
                property_category=random.choice(PropertyCategory.objects.all()),
                property_type=random.choice(PropertyType.objects.all()),
            )
