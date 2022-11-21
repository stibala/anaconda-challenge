from enum import Enum

from sqlalchemy import Column, Integer, Enum as SQLEnum, ForeignKey, String

from app.db_models.base import BaseDBModel


class Symbol(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class Throw(BaseDBModel):
    __tablename__ = "throw"
    id = Column(Integer, primary_key=True)
    turn_id = Column(Integer, ForeignKey("turn.id"))
    username = Column(String(200))
    value = Column(SQLEnum(Symbol, create_constraint=True, validate_strings=True, metadata=BaseDBModel.metadata))
