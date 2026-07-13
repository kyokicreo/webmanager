from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas, file_manager
from app.auth_utils import get_current_user

router = APIRouter()


def log_operation(db: Session, user: models.User, command: str, path: str, success: bool, message: str):
    operation = models.Operation(
        user_id=user.id,
        command=command,
        path=path,
        success=success,
        message=message,
    )
    db.add(operation)
    db.commit()


@router.get("/list-view", response_model=schemas.FileResponse)
def list_files_view(
    path: str = "",
    current_user: models.User = Depends(get_current_user),
):
    try:
        entries = file_manager.list_directory(current_user.username, path)
        return {"success": True, "message": "OK", "data": entries}
    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        return {"success": False, "message": str(e), "data": []}


@router.get("/list", response_model=schemas.FileResponse)
def list_files(
    path: str = "",
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    try:
        entries = file_manager.list_directory(current_user.username, path)
        log_operation(db, current_user, "LIST", path, True, "OK")
        return {"success": True, "message": "OK", "data": entries}
    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        log_operation(db, current_user, "LIST", path, False, str(e))
        return {"success": False, "message": str(e), "data": []}


@router.post("/create", response_model=schemas.FileResponse)
def create_file(
    operation: schemas.FileOperation,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    try:
        file_manager.create_directory(current_user.username, operation.path)
        log_operation(db, current_user, "CREATE", operation.path, True, "Directory created")
        return {"success": True, "message": "Directory created", "data": []}
    except (FileExistsError, ValueError) as e:
        log_operation(db, current_user, "CREATE", operation.path, False, str(e))
        return {"success": False, "message": str(e), "data": []}


@router.post("/delete", response_model=schemas.FileResponse)
def delete_file(
    operation: schemas.FileOperation,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    try:
        file_manager.delete_path(current_user.username, operation.path)
        log_operation(db, current_user, "DELETE", operation.path, True, "Deleted")
        return {"success": True, "message": "Deleted", "data": []}
    except (FileNotFoundError, ValueError, OSError) as e:
        log_operation(db, current_user, "DELETE", operation.path, False, str(e))
        return {"success": False, "message": str(e), "data": []}