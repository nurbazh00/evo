from datetime import date

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    """
        This is a manager for Account class
    """
    def _create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an Email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self._create_user(email=self.normalize_email(email),
                                password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    """
      Custom user class inheriting AbstractBaseUser class
    """

    Male = 'Male'
    Female = 'Female'
    GENDER_CHOICES = [
        (Male, 'Мужчина'),
        (Female, 'Женщина'),
    ]
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    avatar = models.ImageField(upload_to='User',
                               null=True,
                               blank=True,
                               verbose_name='Изображение')
    email = models.EmailField(verbose_name='Почта', max_length=60, unique=True)
    dob = models.DateField(verbose_name='Дата рождения', default=date.today)
    gender = models.CharField(verbose_name='Пол', max_length=7,
                              choices=GENDER_CHOICES, default=Male)
    country = models.CharField(verbose_name='Страна', max_length=255,)
    city = models.CharField(verbose_name='Город', max_length=255,)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
