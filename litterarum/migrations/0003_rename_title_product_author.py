# Generated by Django 4.2 on 2023-04-24 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('litterarum', '0002_product_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='author',
        ),
    ]