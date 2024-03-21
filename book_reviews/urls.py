
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'book_reviews'

urlpatterns = [
    path('datasource/', views.DataTableSourceView.as_view(),
         name='datasource'),
    path('detail/', views.ReviewDetailView.as_view(),
         name='review_details'),
    path('edit/', login_required(views.ReviewDetailView.as_view()),
         name='review_edit'),
    path('add/', login_required(views.ReviewAddView.as_view()),
         name='review_add'),
]
