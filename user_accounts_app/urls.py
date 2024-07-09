from django.urls import path
from allauth.account.views import SignupView, LoginView
from .views import email_confirmation, profile_view

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('email-confirmation/', email_confirmation, name='email_confirmation'),
    path('profile/', profile_view, name='profile'),
]
