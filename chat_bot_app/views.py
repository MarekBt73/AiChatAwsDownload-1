from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from openai import OpenAI


@csrf_exempt
def chat_with_openai(request):
    if request.method == "POST":
        try:
            user_message = request.POST.get("message")
            api_key = config("OPENAI_API_KEY")

            client = OpenAI(api_key=api_key)

            stream = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": user_message}],
                stream=True,
            )

            # Zbieranie całej odpowiedzi z strumienia
            full_response = ""
            for chunk in stream:
                if (
                    chunk.choices
                    and chunk.choices[0].delta
                    and chunk.choices[0].delta.content
                ):
                    full_response += chunk.choices[0].delta.content

            return JsonResponse({"response": full_response})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "This endpoint supports only POST requests."})
