from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    telegram_chat_id = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    operations = relationship("Operation", back_populates="user", cascade="all, delete-orphan")
    telegram_codes = relationship("TelegramLinkCode", cascade="all, delete-orphan")
class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    command = Column(String, nullable=False)
    path = Column(String, nullable=False)
    success = Column(Boolean, nullable=False)
    message = Column(String, nullable=False)

    user = relationship("User", back_populates="operations")

class TelegramLinkCode(Base):
    __tablename__ = "telegram_link_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())