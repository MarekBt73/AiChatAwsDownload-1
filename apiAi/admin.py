from django.contrib import admin
from .models import Chat


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
    list_filter = ["user", "created_at", "model"]
    ordering = ["-created_at"]


admin.site.register(Chat, ChatAdmin)
