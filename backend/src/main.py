import core, services, schemas
from fastapi import FastAPI, Depends
from core.database import get_db
from sqlalchemy.orm import Session
from services.auth import register_user, login_user
from schemas.user import UserCreate, UserLogin

app = FastAPI()

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.email, user.username, user.password)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user.email, user.password)

@app.get("/")
def home():
    return {"message": "Welcome to the University Social Platform"}