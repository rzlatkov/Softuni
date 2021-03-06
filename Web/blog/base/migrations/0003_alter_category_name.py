# Generated by Django 3.2.5 on 2021-08-13 11:15

import base.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210813_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabet and whitespace characters are allowed.'), django.core.validators.MinLengthValidator(3, 'Minimum length of 3 letters required.'), base.validators.validate_capitalized]),
        ),
    ]
