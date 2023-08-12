from django.contrib import admin
from .models import BotUser
from .models import State
from .models import Goods
from .models import Services
from .forms import UsersListForm
from .forms import StateForm
from .forms import GoodsForm
from .forms import ServicesForm


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'telegram_login', 'registration_date')
    # form = UsersListForm


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'description')
    form = GoodsForm


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'description')
    form = GoodsForm


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('telegram_login', 'registration', 'options')

    def telegram_login(self, obj):
        return obj.bot_user.telegram_login

    telegram_login.short_description = 'телеграмм логин'

    # form = StateForm
