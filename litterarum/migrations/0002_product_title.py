# Generated by Django 4.2 on 2023-04-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litterarum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='book title', max_length=200),
        ),
    ]