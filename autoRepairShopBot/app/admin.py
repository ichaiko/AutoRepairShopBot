from django.contrib import admin
from .models import BotUser
from .models import State
from .forms import UsersListForm
from .forms import StateForm


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'telegram_login', 'registration_date')
    # form = UsersListForm


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('bot_user', 'registration')
    # form = StateForm
