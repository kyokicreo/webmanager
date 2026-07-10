from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth_utils import get_current_user

router = APIRouter()


@router.get("/", response_model=list[schemas.HistoryEntry])
def get_history(
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
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
