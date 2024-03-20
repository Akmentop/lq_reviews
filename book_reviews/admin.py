from django.contrib import admin
from .models import ReviewModel

class AdminReviewModel(admin.ModelAdmin):
    exclude = ['date']

admin.site.register(ReviewModel, AdminReviewModel)
