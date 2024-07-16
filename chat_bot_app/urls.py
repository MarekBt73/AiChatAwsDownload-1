from django.urls import path
from .views import chat_with_openai

urlpatterns = [
    path("chat_with_openai/", chat_with_openai, name="chat_with_openai"),
]
