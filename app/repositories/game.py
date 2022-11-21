from fastapi import Depends
from sqlalchemy.orm import Session

from app.api_models.game import GameOut, GameDBIn
from app.db.session import get_db
from app.db_models.game import Game
from app.repositories.base import BaseRepository


class GameRepository(BaseRepository):
    DB_MODEL = Game
    MODEL_IN = GameDBIn
    MODEL_OUT = GameOut


def get_game_repository(session: Session = Depends(get_db)):
    return GameRepository(db_session=session)
