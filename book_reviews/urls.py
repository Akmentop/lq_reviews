from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'book_reviews'

urlpatterns = [
    path('datasource/', views.DataTableSourceView.as_view(), name='datasource'),
    path('detail/', views.ReviewDetailView.as_view(), name='review_details'),
]
