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
        ('Informacje osobiste', {'fields': ('first_name', 'last_name', 'email', 'mobile_phone', 'email_confirmed', 'phone_confirmed')}),
        ('Adres', {'fields': ('address', 'street', 'postal_code', 'city')}),
        ('Informacje szkolne', {'fields': ('subjects', 'school_type', 'grade')}),
        ('Uprawnienia', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Ważne daty', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Informacje osobiste', {'fields': ('first_name', 'last_name', 'email', 'mobile_phone', 'email_confirmed', 'phone_confirmed')}),
        ('Adres', {'fields': ('address', 'street', 'postal_code', 'city')}),
        ('Informacje szkolne', {'fields': ('subjects', 'school_type', 'grade')}),
    )

class StudentActivityAdmin(admin.ModelAdmin):
    list_display = ['uzytkownik', 'typ_aktywnosci', 'opis', 'znacznik_czasu']
    list_filter = ['activity_type', 'timestamp', 'user']

    def uzytkownik(self, obj):
        return obj.user
    uzytkownik.short_description = 'Użytkownik'

    def typ_aktywnosci(self, obj):
        return obj.activity_type
    typ_aktywnosci.short_description = 'Typ aktywności'

    def opis(self, obj):
        return obj.description
    opis.short_description = 'Opis'

    def znacznik_czasu(self, obj):
        return obj.timestamp
    znacznik_czasu.short_description = 'Znacznik czasu'

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['uzytkownik', 'przedmiot', 'procent_postepu', 'ostatnia_aktualizacja']
    list_filter = ['subject', 'progress_percentage', 'last_updated', 'user']

    def uzytkownik(self, obj):
        return obj.user
    uzytkownik.short_description = 'Użytkownik'

    def przedmiot(self, obj):
        return obj.subject
    przedmiot.short_description = 'Przedmiot'

    def procent_postepu(self, obj):
        return obj.progress_percentage
    procent_postepu.short_description = 'Procent postępu'

    def ostatnia_aktualizacja(self, obj):
        return obj.last_updated
    ostatnia_aktualizacja.short_description = 'Ostatnia aktualizacja'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(StudentActivity, StudentActivityAdmin)
admin.site.register(StudentProgress, StudentProgressAdmin)
