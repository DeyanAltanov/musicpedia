from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from musicpedia.accounts.managers import MusicpediaUserManager


class MusicpediaUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = MusicpediaUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        MusicpediaUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *