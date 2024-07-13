from django.utils import timezone  # Importujemy timezone z Django
import logging
from decouple import config
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from openai import OpenAI
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Chat

# Ustaw klucz API OpenAI
api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Konfiguracja loggera
logger = logging.getLogger(__name__)


def ask_openai(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Zmieniono na model "gpt-4-turbo"
            messages=[
                {
                    "role": "system",
                    "content": "Jesteś nauczycielem matematyki w polskiej szkole średniej.",
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
    chats = Chat.objects.filter(user=request.user)

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
    return render(request, "apiAi/chatbot.html", {"chats": chats})
