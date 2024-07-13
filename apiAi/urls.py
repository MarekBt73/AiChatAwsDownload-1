from django.urls import path
from .views import chatbot

urlpatterns = [
    path("chat-2/", chatbot, name="chat_with_gpt-2"),
]
