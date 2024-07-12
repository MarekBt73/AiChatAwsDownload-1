from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Subject, StudentActivity, StudentProgress
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

class StudentActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'description', 'timestamp']
    list_filter = ['activity_type', 'timestamp', 'user']

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'progress_percentage', 'last_updated']
    list_filter = ['subject', 'progress_percentage', 'last_updated', 'user']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(StudentActivity, StudentActivityAdmin)
admin.site.register(StudentProgress, StudentProgressAdmin)
