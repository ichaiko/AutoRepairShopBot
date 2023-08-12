from django.db import models


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


class Goods(models.Model):
    name = models.CharField(
        max_length=30, null=True, verbose_name='Наименование товара'
    )

    price = models.IntegerField(
        verbose_name='Цена товара',
        null=True
    )

    image = models.ImageField(
        null=True, blank=True, upload_to='images/'
    )

    description = models.TextField(
        null=True, verbose_name="Описание товара", blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Services(models.Model):
    name = models.CharField(
        max_length=30, null=True, verbose_name='Наименование услуги'
    )

    price = models.IntegerField(
        verbose_name='Стоимость услуги',
        null=True
    )

    description = models.TextField(
        null=True, verbose_name="Описание товара", blank=True
    )

    image = models.ImageField(
        null=True, blank=True, upload_to='images/'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class State(models.Model):
    bot_user = models.ForeignKey(
        BotUser,
        verbose_name="id пользователя",
        on_delete=models.CASCADE,
        null=True
    )

    registration = models.BooleanField(
        verbose_name='На регистрации', null=True,
        default=False,
        choices=((True, 'Да'), (False, 'Нет'))
    )

    options = models.BooleanField(
        verbose_name='На выборе товаров/услуг', null=True,
        default=False,
        choices=((True, 'Да'), (False, 'Нет'))
    )

    class Meta:
        verbose_name = "Состояние пользователя"
        verbose_name_plural = "Состояние пользователей"
