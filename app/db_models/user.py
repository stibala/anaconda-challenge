from sqlalchemy import Column, Integer, String, Boolean
from app.db_models.base import BaseDBModel


class User(BaseDBModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False, unique=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    hashed_password = Column(String(200), nullable=False)
    disabled = Column(Boolean, default=False)
