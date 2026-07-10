from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
class FileOperation(BaseModel):
    path: str = ""


class FileResponse(BaseModel):
    success: bool
    message: str
    data: list[str] = []


class HistoryEntry(BaseModel):
    timestamp: datetime
    username: str
    command: str
    path: str
    success: bool
    message: str

    class Config:
        from_attributes = True