# Generated by Django 4.1.3 on 2022-11-17 06:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atom', '0004_alter_marks_telugu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='Telugu',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
