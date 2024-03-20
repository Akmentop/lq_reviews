from django.contrib import admin
from .models import Review

class AdminReview(admin.ModelAdmin):
    exclude = ['date']

admin.site.register(Review, AdminReview)
