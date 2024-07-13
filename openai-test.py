from openai import OpenAI
from decouple import config


# Pobierz klucz API z pliku .env
api_key = config("OPENAI_API_KEY")
print(api_key)


OPENAI_API_KEY = config("OPENAI_API_KEY")

print(f"OpenAI API Key from settings: {OPENAI_API_KEY}")

# Utwórz klienta OpenAI z kluczem API
client = OpenAI(api_key="sk-None-ux1xxkAwFDO5EDjolF6CT3BlbkFJz5UJmcufMieVxjeI45pa")


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

print(completion.choices[0].message)
