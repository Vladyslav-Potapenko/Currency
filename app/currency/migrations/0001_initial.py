# Generated by Django 4.2.2 on 2023-08-11 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.CharField(max_length=256, validators=[django.core.validators.EmailValidator], verbose_name='Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.CharField(max_length=300, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('request_method', models.CharField(max_length=100)),
                ('time', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('source_url', models.URLField(max_length=255, verbose_name='URL')),
                ('phone', models.CharField(max_length=13, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy')),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('currency', models.PositiveSmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=1, verbose_name='Currency')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.source')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
    ]
