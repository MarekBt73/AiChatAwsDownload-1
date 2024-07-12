from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('imie', 'email', 'data_utworzenia')
    search_fields = ('imie', 'email')
    readonly_fields = ('imie', 'email', 'wiadomosc', 'data_utworzenia')

    def imie(self, obj):
        return obj.name
    imie.short_description = 'Imię'

    def data_utworzenia(self, obj):
        return obj.created_at
    data_utworzenia.short_description = 'Data utworzenia'

    def wiadomosc(self, obj):
        return obj.message
    wiadomosc.short_description = 'Wiadomość'
