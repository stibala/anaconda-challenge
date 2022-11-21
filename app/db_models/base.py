"""Base DB model"""

from app.db.base import Base


class BaseDBModel(Base):
    """Base model"""
    __abstract__ = True
