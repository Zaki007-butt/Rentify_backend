# Generated by Django 5.0.6 on 2025-01-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0017_utilitybill"),
    ]

    operations = [
        migrations.AddField(
            model_name="utilitybill",
            name="payment_receipt",
            field=models.ImageField(
                blank=True,
                help_text="Payment receipt image",
                null=True,
                upload_to="bills/receipts/",
            ),
        ),
    ]
