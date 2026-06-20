from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.api.auth import router

from app.models.user import User

from app.api.interview import router as interview_router

from app.api.upload import router as upload_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "API Running"
    }



app.include_router(
    interview_router
)

app.include_router(
    upload_router
)