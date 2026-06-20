from fastapi import APIRouter
from fastapi import Depends

from app.core.security import get_current_user

from fastapi import APIRouter

from pydantic import BaseModel

from app.services.question_generator import generate_questions

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)

@router.get("/dashboard")
def dashboard(

    user=Depends(
        get_current_user
    )

):

    return {

        "message":"Welcome",

        "user":user

    }



class InterviewRequest(
    BaseModel
):

    role: str

    difficulty: str

    skills: list[str]


@router.post("/generate")
def generate(
    data: InterviewRequest
):

    questions = generate_questions(
        data.role,
        data.difficulty,
        data.skills
    )

    return questions