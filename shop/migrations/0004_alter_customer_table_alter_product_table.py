# Generated by Django 4.0.5 on 2022-07-05 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
