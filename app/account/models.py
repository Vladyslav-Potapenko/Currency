import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static


def avatar_path(instance, filename):
    return f'avatars/user_{instance.id}/{filename}'


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('Phone'), null=True, max_length=13)
    avatar = models.FileField(
        _('Avatar'),
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def avatar_url(self) -> str:
        if self.avatar:
            return self.avatar.url

        return static('users/721495.png')

    def save(self, *args, **kwargs):
        if not self.pk and not self.username:
            self.username = str(uuid.uuid4())

        super().save(*args, **kwargs)
