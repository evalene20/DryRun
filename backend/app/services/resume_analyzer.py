import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the resume and return ONLY valid JSON.

Required format:

{{
    "skills": [],
    "projects": [],
    "experience_level": "",
    "strengths": [],
    "missing_skills": [],
    "resume_score": 0
}}

Resume:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = response.text.strip()

    if result.startswith("```json"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    try:
        return json.loads(result)

    except Exception:
        return {
            "raw_response": result
        }