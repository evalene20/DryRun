import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_json_response(text: str):

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def generate_questions(
    role,
    difficulty,
    skills
):

    prompt = f"""
Generate interview questions.

Role: {role}

Difficulty: {difficulty}

Skills: {", ".join(skills)}

Return ONLY valid JSON.

{{
    "technical_questions": [],
    "project_questions": [],
    "hr_questions": []
}}

Rules:
- Exactly 5 technical questions
- Exactly 3 project questions
- Exactly 2 HR questions
- No explanations
- No markdown
- JSON only
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = clean_json_response(
        response.text
    )

    try:
        return json.loads(result)

    except Exception as e:

        print("JSON Parse Error:", e)
        print("Gemini Response:", result)

        return {
            "Technical questions": [],
            "Project questions": [],
            "HR questions": []
        }


def generate_resume_questions(
    analysis
):

    prompt = f"""
Generate interview questions based on this resume.

Skills:
{analysis.get("skills", [])}

Projects:
{analysis.get("projects", [])}

Experience Level:
{analysis.get("experience_level", "")}

Return ONLY valid JSON.

{{
    "Technical questions": [],
    "Project questions": [],
    "HR questions": []
}}

Rules:
- Exactly 5 technical questions
- Exactly 3 project questions
- Exactly 2 HR questions
- Questions must be specific to the resume
- No explanations
- No markdown
- JSON only
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = clean_json_response(
        response.text
    )

    try:
        return json.loads(result)

    except Exception as e:

        print("JSON Parse Error:", e)
        print("Gemini Response:", result)

        return {
            "Technical questions": [],
            "Project questions": [],
            "HR questions": []
        }