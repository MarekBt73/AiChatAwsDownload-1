from openai import OpenAI
from decouple import config

# Pobierz klucz API z pliku .env
api_key = config("OPENAI_API_KEY")

# Utwórz klienta OpenAI z kluczem API
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion["choices"][0]["message"]["content"])
