# Generated by Django 4.0.3 on 2022-03-09 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='images',
        ),
    ]