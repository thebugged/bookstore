# Generated by Django 4.2 on 2023-04-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litterarum', '0004_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]