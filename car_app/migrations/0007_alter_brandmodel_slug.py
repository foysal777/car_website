# Generated by Django 5.0.6 on 2024-06-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0006_alter_brandmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(default='my_slug', max_length=100),
        ),
    ]
