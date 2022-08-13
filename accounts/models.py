from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        # convert all in lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, username, password, **other_fields)


class Accounts(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(_('email address'), max_length=32, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    # required for superuser
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'