from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Chat


class UserConversationFilter(admin.SimpleListFilter):
    title = _("user conversation")
    parameter_name = "user_conversation"

    def lookups(self, request, model_admin):
        # Tutaj możesz zdefiniować, jakie opcje filtru będą dostępne.
        # Na przykład, możesz zwrócić listę użytkowników.
        users = set([c.user for c in model_admin.model.objects.all()])
        return [(u.id, u.username) for u in users]

    def queryset(self, request, queryset):
        # Tutaj definiujesz, jak filtr ma wpływać na queryset.
        if self.value():
            return queryset.filter(user__id__exact=self.value())
        else:
            return queryset


class ChatAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "message",
        "response",
        "model",
        "usage",
        "response_id",
        "created_at",
    ]
    list_filter = [UserConversationFilter, "created_at", "model"]
    ordering = ["-created_at"]


admin.site.register(Chat, ChatAdmin)
