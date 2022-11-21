from app.api_models.base import BaseAPIModel
from typing import Optional, List

from app.api_models.throw import ThrowOut


class Turn(BaseAPIModel):
    game_id: int


class TurnIn(Turn):
    ...


class TurnOut(Turn):
    id: int
    winner: Optional[str]
    finished: bool
    throws: List[ThrowOut]

    class Config:
        orm_mode = True
