from fastapi import APIRouter
from pydantic import BaseModel

from app.services.question_generator import (
    generate_questions,
    generate_resume_questions
)

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


class InterviewRequest(BaseModel):
    role: str
    difficulty: str
    skills: list[str]


@router.post("/generate")
def generate(data: InterviewRequest):

    questions = generate_questions(
        data.role,
        data.difficulty,
        data.skills
    )

    return questions


@router.post("/resume-questions")
def resume_questions(
    analysis: dict
):

    return generate_resume_questions(
        analysis
    )