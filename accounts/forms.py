
from django import forms


class UserForm(forms.Form):
    """For validating username and password of signup and login."""

    username = forms.CharField(label='User Name', max_length=32, min_length=4)
    password = forms.CharField(label='Password', max_length=64, min_length=4)

