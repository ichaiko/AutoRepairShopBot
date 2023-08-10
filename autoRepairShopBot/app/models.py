from django.db import models


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
