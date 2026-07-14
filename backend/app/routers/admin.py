from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas, auth_utils
from app.auth_utils import require_admin, require_superadmin

router = APIRouter()


@router.get("/users", response_model=list[schemas.UserOut])
def list_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin),
):
    return db.query(models.User).all()


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_superadmin),
):
    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="Нельзя удалить самого себя")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    db.delete(user)
    db.commit()
    return {"success": True, "message": f"Пользователь {user.username} удалён"}

@router.post("/users/{user_id}/reset-password")
def reset_password(
    user_id: int,
    new_password: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_admin),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if user.role in ("admin", "superadmin") and current_user.role != "superadmin" and user.id != current_user.id:
        raise HTTPException(status_code=403, detail="Только главный администратор может менять пароли администраторов")

    user.password_hash = auth_utils.hash_password(new_password)
    db.commit()
    return {"success": True, "message": f"Пароль пользователя {user.username} изменён"}


@router.post("/users/{user_id}/promote")
def promote_to_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_superadmin),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user.role = "admin"
    db.commit()
    return {"success": True, "message": f"Пользователь {user.username} назначен администратором"}