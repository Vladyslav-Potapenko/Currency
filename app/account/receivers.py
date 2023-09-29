import re
from django.db.models.signals import pre_save
from django.dispatch import receiver
from account.models import User


@receiver(pre_save, sender=User)
def user_phone(instance, *args, **kwargs):
    if instance.phone:
        instance.phone = re.sub(r'\D', '', instance.phone)
