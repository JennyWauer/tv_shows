# Generated by Django 2.2 on 2021-01-01 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
