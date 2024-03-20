from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'blurb', 'cost', 'name', 'photo', 'review']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
