from django.urls import path
from .views import chatbot, start_new_chat

urlpatterns = [
    path("chat-2/", chatbot, name="chat_with_gpt-2"),
    path("start-new-chat/", start_new_chat, name="start_new_chat"),
]
