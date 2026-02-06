from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserRead
from app.services.user_service import create_fake_user

app = FastAPI()

@app.post("/create-fake-user", response_model=UserRead)
def create_user_for_testing(db: Session = Depends(get_db)):
    return create_fake_user(db)
