# Generated by Django 5.0.7 on 2024-09-03 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]