from typing import List, Optional

from app.api_models.base import BaseAPIModel


class Game(BaseAPIModel):
    first_user_name: str
    second_user_name: str


class GameIn(BaseAPIModel):
    other_user_name: Optional[str]


class GameDBIn(Game):
    ...


class GameOut(Game):
    id: int
    turn_ids: List[int]

    class Config:
        orm_mode = True
