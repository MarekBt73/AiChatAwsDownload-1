from django.db import models
from django.conf import settings


class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    model = models.CharField(max_length=50, default="gpt-3.5-turbo")
    usage = models.JSONField(default=dict)
    response_id = models.CharField(
        max_length=50, null=True, blank=True
    )  # Pozwala na null/blank, aby można było ustawić później
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessage from {self.user.username} at {self.created_at}"
