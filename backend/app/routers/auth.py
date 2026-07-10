from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas, auth_utils

router = APIRouter()


@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")

    hashed_password = auth_utils.hash_password(user.password)
    new_user = models.User(username=user.username, password_hash=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not db_user or not auth_utils.verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

    access_token = auth_utils.create_access_token(data={"user_id": db_user.id, "username": db_user.username})

    return {"access_token": access_token, "token_type": "bearer"}