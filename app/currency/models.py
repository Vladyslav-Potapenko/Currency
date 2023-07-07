from django.db import models
from django.core.validators import EmailValidator


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField()
    currency_type = models.CharField(max_length=3)
    source = models.CharField(max_length=68)


class Contact_us(models.Model):
    email_from = models.CharField(max_length=256, validators=[EmailValidator])
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
