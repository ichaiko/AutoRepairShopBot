from django.db import models

class UsersList(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="id пользователя"
    )

    login = models.CharField(
        max_length=30, null=True, verbose_name="telegram-логин пользователя"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"