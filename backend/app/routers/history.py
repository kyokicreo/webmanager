from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth_utils import get_current_user

router = APIRouter()


def build_history_response(db: Session, current_user: models.User, limit: int):
    operations = (
        db.query(models.Operation)
        .join(models.User)
        .filter(models.Operation.user_id == current_user.id)
        .order_by(models.Operation.timestamp.desc())
        .limit(limit)
        .all()
    )

    result = []
    for op in operations:
        result.append(
            schemas.HistoryEntry(
                timestamp=op.timestamp,
                username=op.user.username,
                command=op.command,
                path=op.path,
                success=op.success,
                message=op.message,
            )
        )
    return result


@router.get("/", response_model=list[schemas.HistoryEntry])
def get_history(
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    result = build_history_response(db, current_user, limit)

    operation = models.Operation(
        user_id=current_user.id,
        command="HISTORY",
        path="",
        success=True,
        message="OK",
    )
    db.add(operation)
    db.commit()

    return result


@router.get("/view", response_model=list[schemas.HistoryEntry])
def get_history_view(
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return build_history_response(db, current_user, limit)