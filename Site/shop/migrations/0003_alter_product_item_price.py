# Generated by Django 4.1.7 on 2023-04-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
