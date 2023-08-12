from django import forms
from .models import BotUser
from .models import State
from .models import Goods


class UsersListForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = (
            'telegram_id',
            'telegram_login',
        )


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = (
            'registration',
        )


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = (
            'name',
            'price',
            'description'
        )
