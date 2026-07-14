import secrets
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.auth_utils import get_current_user

router = APIRouter()

BOT_USERNAME = "fullstaker_bot"


@router.post("/link-code")
def generate_link_code(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    code = secrets.token_urlsafe(8)

    link_code = models.TelegramLinkCode(code=code, user_id=current_user.id)
    db.add(link_code)
    db.commit()

    return {"link": f"https://telegram.me/{BOT_USERNAME}?start={code}"}