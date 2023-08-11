from django.contrib import admin
from .models import BotUser
from .models import State
from .forms import UsersListForm
from .forms import StateForm


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ('id', 'external_id', 'login')
    form = UsersListForm


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    # list_display = ('registration',)
    form = StateForm
