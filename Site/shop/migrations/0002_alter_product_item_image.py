# Generated by Django 4.1.7 on 2023-03-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_item',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]