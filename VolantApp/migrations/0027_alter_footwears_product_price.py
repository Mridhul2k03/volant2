# Generated by Django 5.0.6 on 2024-06-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VolantApp', '0026_alter_footwears_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footwears',
            name='product_price',
            field=models.FloatField(),
        ),
    ]
