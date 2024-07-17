import logging
from decouple import config
from openai import OpenAI
import markdown

# Ustaw klucz API OpenAI
api_key = config("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Konfiguracja loggera
logger = logging.getLogger(__name__)


def ask_openai(user_name, school_type, grade, message, first_message=False):
    try:
        system_message_content = (
            f"You are a mathematics teacher in a Polish high school. "
            f"The student you are talking to is in {school_type}, grade {grade}. "
            f"Your students are aged between 11 and 14 years old. "
            f"Answer their questions in a concise, clear, and understandable manner for technical school students. "
            f"Provide only the necessary calculations and the final result. "
            f"Explain how you performed the calculations in a simplified manner appropriate for their age. "
            f"Use '*' for multiplication, '/' for division, '+' for addition, and '-' for subtraction, as commonly used in schools. "
            f"If necessary, use a special font for mathematical equations. "
            f"Use '=' for equality and '≈' for approximations instead of '~='. "
            f"Use '^' for exponentiation. "
            f"Use normal parentheses '(' and ')' instead of '\\('. "
            f"Do not use LaTeX-style fractions like '\\frac'. "
            f"Do not display '\\)'. "
            f"Respond in Polish. "
            f"Format the response in Markdown. "
            f"Explain step by step how you performed the calculation or which formulas you used and what you were guided by. "
            f"Refer to the theory on which you base the solution. "
            f"Use bold or bullet points when answering a question to make the answer readable. You can use Tailwind CSS classes. "
            f"Always address the student by their name, {user_name}, at the beginning of your response. "
            f"Write mathematical expressions (e.g., c^2 = a^2 + b^2) in a way that is clear and understandable for elementary or high school students. "
            f"Use common mathematical symbols such as those shown in the attached graphic file. "
        )

        if first_message:
            system_message_content += f"Ask the student how they are coping with mathematics and if they have any specific problems."

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_message_content},
                {"role": "user", "content": message},
            ],
            temperature=0.3,
            # max_tokens=250,
        )
        answer = response.choices[0].message.content.strip()
        html_answer = markdown.markdown(answer)
        return html_answer
    except Exception as e:
        logger.error(f"Error in OpenAI API call: {e}")
        return "Sorry, there was an error processing your request."
