import os
import json

from google import genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)


def generate_questions(
    role,
    difficulty,
    skills
):

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Generate 10 interview questions.

Role:
{role}

Difficulty:
{difficulty}

Skills:
{skills}

Return JSON only.

Format:

{{
    "questions": []
}}
"""

    response = model.generate_content(
        prompt
    )

    return json.loads(
        response.text
    )