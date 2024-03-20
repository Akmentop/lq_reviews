from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import ReviewModel


class ReviewForm(ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['author', 'blurb', 'cost', 'name', 'photo', 'review']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
