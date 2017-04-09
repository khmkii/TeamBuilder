from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from projects.models import Profile


class SiteUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("You must supple a username!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        Profile.objects.create(
            user=user,
            slug=username,
        )

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class SiteUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = SiteUserManager()
    users = objects

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_short_name(self):
        # make this more usefull
        return f'{self.username}'

    def get_full_name(self):
        # make this more usefull
        return f'{self.username} {self.email}'
