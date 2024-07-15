from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm as AllauthSignupForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "address",
            "street",
            "postal_code",
            "city",
            "mobile_phone",
            "subjects",
            "school_type",
            "grade",
            "email_confirmed",
            "phone_confirmed",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "address",
            "street",
            "postal_code",
            "city",
            "mobile_phone",
            "subjects",
            "school_type",
            "grade",
            "email_confirmed",
            "phone_confirmed",
        )


class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _("Użytkownik o tym adresie e-mail już istnieje.")
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Użytkownik o tej nazwie już istnieje."))
        return username


class CustomSignupForm(AllauthSignupForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")
        # Sprawdzenie, czy adres e-mail już istnieje w bazie danych
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email
