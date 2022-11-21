from fastapi import Depends
from sqlalchemy.orm import Session

from app.api_models.turn import TurnIn, TurnOut
from app.db.session import get_db
from app.db_models import Turn
from app.repositories.base import BaseRepository


class TurnRepository(BaseRepository):
    DB_MODEL = Turn
    MODEL_IN = TurnIn
    MODEL_OUT = TurnOut


def get_turn_repository(session: Session = Depends(get_db)):
    return TurnRepository(db_session=session)
