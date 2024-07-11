from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Subject
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'mobile_phone', 'is_staff', 'is_active', 'email_confirmed', 'phone_confirmed']
    list_filter = ['subjects', 'is_staff', 'is_active', 'email_confirmed', 'phone_confirmed']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile_phone', 'email_confirmed', 'phone_confirmed')}),
        ('Address', {'fields': ('address', 'street', 'postal_code', 'city')}),
        ('School info', {'fields': ('subjects', 'school_type', 'grade')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile_phone', 'email_confirmed', 'phone_confirmed')}),
        ('Address', {'fields': ('address', 'street', 'postal_code', 'city')}),
        ('School info', {'fields': ('subjects', 'school_type', 'grade')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
