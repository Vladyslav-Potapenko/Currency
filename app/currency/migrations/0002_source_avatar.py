# Generated by Django 4.2.2 on 2023-08-14 15:46

import currency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to=currency.models.logo_path, verbose_name='Logo'),
        ),
    ]