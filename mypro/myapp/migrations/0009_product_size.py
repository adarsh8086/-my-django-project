# Generated by Django 5.0.7 on 2024-09-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='Medium', max_length=50),
            preserve_default=False,
        ),
    ]
