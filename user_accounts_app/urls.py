from django.urls import path
from .views import (
    CustomSignupView,
    email_confirmation,
    profile_view,
    edit_profile_view,
    chat_detail_view,
)
from allauth.account.views import LoginView

urlpatterns = [
    path("register/", CustomSignupView.as_view(), name="account_signup"),
    path("login/", LoginView.as_view(), name="account_login"),
    path("email-confirmation/", email_confirmation, name="email_confirmation"),
    path("profile/", profile_view, name="profile"),
    path("profile/chat/<int:chat_id>/", chat_detail_view, name="chat_detail"),
    path("profile/edit/", edit_profile_view, name="edit_profile"),
]
