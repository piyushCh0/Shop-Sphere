# Generated by Django 5.1.1 on 2024-09-10 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
