from django.db import models
from django.conf import settings
import uuid


class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    model = models.CharField(max_length=50, default="gpt-4-turbo")
    usage = models.JSONField(default=dict)
    response_id = models.CharField(
        max_length=50, null=True, blank=True
    )  # Pozwala na null/blank, aby można było ustawić później
    session_id = models.UUIDField(
        default=uuid.uuid4, editable=False
    )  # Nowe pole session_id
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessage from {self.user.username} at {self.created_at}"
