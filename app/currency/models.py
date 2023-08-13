from django.db import models
from django.core.validators import EmailValidator
from currency.choices import RateCurrencyChoices
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency = models.PositiveSmallIntegerField(_('Currency'),
                                                choices=RateCurrencyChoices.choices,
                                                default=RateCurrencyChoices.USD
                                                )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = ('Rate')
        verbose_name_plural = ('Rates')


class Contact_us(models.Model):
    email_from = models.CharField(_('Email'), max_length=256, validators=[EmailValidator])
    subject = models.CharField(_('Subject'), max_length=100)
    message = models.CharField(_('Message'), max_length=300)

    class Meta:
        verbose_name = ('Contact Us')
        verbose_name_plural = ('Contact Us')


class Source(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    source_url = models.URLField(_('URL'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=13)

    class Meta:
        verbose_name = ('Source')
        verbose_name_plural = ('Sources')

    def __str__(self):
        return self.name



class RequestResponseLog(models.Model):
    path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=100)
    time = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
