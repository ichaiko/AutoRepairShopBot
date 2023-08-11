from django import forms
from .models import BotUser
from .models import State


class UsersListForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = (
            'telegram_id',
            'telegram_login'
        )


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = (
            'registration',
        )
