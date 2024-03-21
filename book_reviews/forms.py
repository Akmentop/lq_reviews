from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Review


class ReviewAddForm(ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'blurb', 'cost', 'name', 'photo', 'review']

