# Generated by Django 2.1.7 on 2019-04-14 02:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Phone numbers must be 10 digits.', regex='^\\+?1?\\d{10}$')]),
        ),
    ]
