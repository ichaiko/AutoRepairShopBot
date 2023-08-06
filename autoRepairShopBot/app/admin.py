from django.contrib import admin
from .models import UsersList
from .forms import UsersListForm


@admin.register(UsersList)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ('id', 'external_id', 'login')
    form = UsersListForm
