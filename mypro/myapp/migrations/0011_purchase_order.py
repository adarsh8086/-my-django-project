# Generated by Django 5.0.7 on 2024-09-30 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='myapp.order'),
        ),
    ]
