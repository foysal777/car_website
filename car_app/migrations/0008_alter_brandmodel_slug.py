# Generated by Django 5.0.6 on 2024-06-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0007_alter_brandmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
