# Generated by Django 5.0.6 on 2024-07-08 23:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_rename_rent_or_sale_property_rent_or_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='Sialkot', max_length=100, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]