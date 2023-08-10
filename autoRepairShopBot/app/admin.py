from django.contrib import admin
from .models import BotUser
from .forms import UsersListForm


@admin.register(BotUser)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ('id', 'external_id', 'login')
    form = UsersListForm
