

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',  views.UserSignupView.as_view(), name='ajax_signup'),
    path('login/',  views.UserLoginView.as_view(), name='ajax_login'),
    path('logout/',  views.UserLogoutView.as_view(), name='ajax_logout'),
]
