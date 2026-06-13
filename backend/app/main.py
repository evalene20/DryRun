from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.api.auth import router

from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "API Running"
    }