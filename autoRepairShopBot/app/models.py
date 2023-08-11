from django.db import models
from django.utils import timezone


class BotUser(models.Model):
    registration_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время регистрации",
        null=True
    )

    telegram_id = models.BigIntegerField(
        verbose_name="id пользователя",
        unique=True,
        null=True,
    )

    telegram_login = models.CharField(
        max_length=30, null=True, verbose_name="логин пользователя"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class State(models.Model):
    bot_user = models.ForeignKey(
        BotUser,
        verbose_name="id пользователя",
        on_delete=models.CASCADE,
        null=True
    )

    registration = models.BooleanField(
        verbose_name='На регистрации', null=True,
        default=False, choices=((True, 'Да'), (False, 'Нет'))
    )

    class Meta:
        verbose_name = "Состояние пользователя"
        verbose_name_plural = "Состояние пользователей"
