from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

from book_reviews.utils import shorten


class Review(models.Model):

    NO_IMG_AVAILABLE_IMG = 'icons/review_small.png'

    author = models.CharField(max_length=128)
    blurb = models.TextField(blank=False, null=False)
    cost = models.DecimalField(
        decimal_places=2, max_digits=6)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=128, blank=False, null=False)
    photo = models.ImageField(
        blank=False, default=NO_IMG_AVAILABLE_IMG, upload_to='photos/')
    review = models.TextField(blank=False, null=False)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                     on_delete=models.CASCADE)

    def get_info_as_list(self, summary=True) -> list:
        if summary:
            self.blurb = shorten(self.blurb)
            self.review = shorten(self.review)
        return [[
            self.photo.url,
            self.blurb,
            self.cost,
            self.date.strftime('%Y-%m-%d'),
            self.name,
            self.review,
            self.submitted_by_id,
        ], self.id,]
    
    def get_review_summary(self) -> str:
        return self.review[:100] + ('...' if len(self.review) > 100 else '')



    def get_as_recent(self) -> str:
        return [self.photo.url, self.date.strftime('%Y-%m-%d'), self.name, self.get_review_summary(), self.id]
    
    class Meta:
        ordering = ['-date', '-id']
        