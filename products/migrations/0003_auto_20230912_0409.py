# Generated by Django 3.2.7 on 2023-09-12 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
