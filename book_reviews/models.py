from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class ReviewModel(models.Model):

    NO_IMG_AVAILABLE_IMG = 'static/icons/review_small.png'

    author = models.CharField(max_length=128)
    blurb = models.TextField(blank=False, null=False)
    cost = models.FloatField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    # last_modified = models.DateField()
    name = models.TextField(blank=False, null=False)
    photo = models.ImageField(blank=False, default=NO_IMG_AVAILABLE_IMG,
                              upload_to='photos/')
    review = models.TextField(blank=False, null=False)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                     on_delete=models.CASCADE)


