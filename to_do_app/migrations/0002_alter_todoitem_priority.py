# Generated by Django 4.2 on 2023-07-11 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
