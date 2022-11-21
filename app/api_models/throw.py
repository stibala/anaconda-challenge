from typing import Optional

from app.api_models.base import BaseAPIModel
from app.db_models.throw import Symbol


class Throw(BaseAPIModel):
    turn_id: int


class ThrowIn(Throw):
    value: Optional[Symbol]


class ThrowDBIn(ThrowIn):
    username: str


class ThrowOut(Throw):
    value: Symbol
    username: str
    id: int

    class Config:
        orm_mode = True
