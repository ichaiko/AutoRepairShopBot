from django import forms
from .models import UsersList


class UsersListForm(forms.ModelForm):
    class Meta:
        model = UsersList
        fields = (
            'external_id',
            'login'
        )
