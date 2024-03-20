"""
URL configuration for lq_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import book_reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_reviews.views.HomePageView.as_view()),
    path('datasource/', book_reviews.views.dt_data),
    path('detail/<int:review_id>', book_reviews.views.detail),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
