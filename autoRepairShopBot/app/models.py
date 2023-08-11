from django.db import models
from django.utils import timezone


class BotUser(models.Model):

    telegram_id = models.BigIntegerField(
        verbose_name="id пользователя",
        unique=True,
        null=True
    )

    telegram_login = models.CharField(
        max_length=30, null=True, verbose_name="логин пользователя"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class State(models.Model):
    registration = models.BooleanField(
        verbose_name='На регистрации', null=False,
        default=False, choices=((True, 'Да'), (False, 'Нет'))
    )

    class Meta:
        verbose_name = "Состояние пользователя"
        verbose_name_plural = "Состояние пользователей"
