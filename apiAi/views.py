from django.utils import timezone  # Importujemy timezone z Django
import logging
from decouple import config
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from openai import OpenAI
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Chat
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

# Ustaw klucz API OpenAI
api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
from django.core.paginator import Paginator

# Konfiguracja loggera
logger = logging.getLogger(__name__)


def ask_openai(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Zmieniono na model "gpt-4-turbo"
            messages=[
                {
                    # The `"role": "system"` and accompanying content in the `ask_openai` function are
                    # part of the input messages provided to the OpenAI API for generating responses.
                    # In this specific context, it sets the role as "system" and provides a prompt for
                    # the AI model to simulate a scenario where the user is a mathematics teacher in a
                    # Polish high school. The prompt instructs the AI to answer students' questions
                    # concisely, provide necessary calculations and final results, explain the
                    # calculations in a simplified manner without excessive details, and respond in
                    # Polish.
                    "role": "system",
                    "content": (
                        "You are a mathematics teacher in a Polish high school. "
                        "Your students are aged between 11 and 14 years old. "
                        "Answer their questions in a concise, clear, and understandable manner for technical school students. "
                        "Provide only the necessary calculations and the final result. "
                        "Explain how you performed the calculations in a simplified manner appropriate for their age. "
                        "Use '×' for multiplication instead of '*'. "
                        "Use '÷' for division instead of '/'. "
                        "Use '=' for equality and '≈' for approximations instead of '~='. "
                        "Use '^' for exponentiation. "
                        "Use normal parentheses '(' and ')' instead of '\\('. "
                        "Do not use LaTeX-style fractions like '\\frac'. "
                        "Do not display '\\)'. "
                        "Respond in Polish."
                    ),
                },
                {"role": "user", "content": message},
            ],
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        logger.error(f"Error in OpenAI API call: {e}")
        return "Sorry, there was an error processing your request."


@login_required  # Przeniesienie dekoratora na widok
@csrf_protect
def chatbot(request):
    chat_list = Chat.objects.filter(user=request.user).order_by("-created_at")
    paginator = Paginator(chat_list, 10)  # Paginacja, 10 wiadomości na stronę

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)

        chat = Chat(
            user=request.user,
            message=message,
            response=response,
            created_at=timezone.now(),  # Użycie Django timezone
        )
        chat.save()
        return JsonResponse({"message": message, "response": f"<pre>{response}</pre>"})

    return render(request, "apiAi/chatbot.html", {"page_obj": page_obj})


@login_required
@csrf_protect
def start_new_chat(request):
    # Usunięcie wszystkich wiadomości użytkownika
    Chat.objects.filter(user=request.user).delete()
    return redirect(reverse("chat_with_gpt-2"))
