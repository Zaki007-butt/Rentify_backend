# Generated by Django 5.0.6 on 2024-12-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0015_propertyimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("completed", "Completed"),
                    ("failed", "Failed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]