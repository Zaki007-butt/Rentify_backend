# Generated by Django 5.0.6 on 2024-07-07 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_property_rent_or_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='rent_or_sale',
            new_name='rent_or_buy',
        ),
    ]
