from django import forms
from .models import BotUser


class UsersListForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = (
            'telegram_id',
            'telegram_login'
        )
