# Generated by Django 4.2.4 on 2023-08-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_state_options_state_goods_state_services_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='availability',
            field=models.IntegerField(null=True, verbose_name='Количество товара в наличии'),
        ),
    ]
