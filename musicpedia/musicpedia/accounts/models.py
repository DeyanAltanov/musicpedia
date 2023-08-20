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
    MALE = 'Male'
    FEMALE = 'Female'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0, blank=True)
    gender = models.CharField(choices=GENDER, blank=True)

    user = models.OneToOneField(
        MusicpediaUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *