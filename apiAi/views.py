from django.utils import timezone  # Importujemy timezone z Django
import logging
from decouple import config
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Chat
from django.urls import reverse
from user_accounts_app.models import CustomUser  # Poprawny import
from .utils import ask_openai
from django.core.paginator import Paginator

# Konfiguracja loggera
logger = logging.getLogger(__name__)


@login_required
@csrf_protect
def chatbot(request):
    chat_list = Chat.objects.filter(user=request.user).order_by(
        "created_at"
    )  # Sortowanie od najstarszej do najnowszej
    paginator = Paginator(chat_list, 10)  # Paginacja, 10 wiadomości na stronę

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    user = request.user
    user_name = user.first_name if user.first_name else user.username

    # Pobierz typ szkoły i klasę z profilu użytkownika
    school_type = (
        user.get_school_type_display() if user.school_type else "Unknown school type"
    )
    grade = user.grade if user.grade else "Unknown grade"

    if request.method == "POST":
        message = request.POST.get("message")
        # Sprawdź, czy jest to pierwsza wiadomość w konwersacji
        first_message = not Chat.objects.filter(user=request.user).exists()

        response = ask_openai(
            user_name, school_type, grade, message, first_message
        )  # Przekazanie dodatkowych danych do ask_openai

        chat = Chat(
            user=request.user,
            message=message,
            response=response,
            created_at=timezone.now(),  # Użycie Django timezone
        )
        chat.save()
        return JsonResponse({"message": message, "response": response})

    return render(request, "apiAi/chatbot.html", {"page_obj": page_obj})


@login_required
@csrf_protect
def start_new_chat(request):
    # Usunięcie wszystkich wiadomości użytkownika
    Chat.objects.filter(user=request.user).delete()
    return redirect(reverse("chat_with_gpt-2"))
