from django.utils.translation import gettext_lazy as _  # noqa F401

from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, ('Dollar')
    EUR = 2, ('Euro')
