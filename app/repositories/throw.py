from fastapi import Depends
from sqlalchemy.orm import Session

from app.api_models.throw import ThrowIn, ThrowOut
from app.db.session import get_db
from app.db_models import Throw
from app.repositories.base import BaseRepository


class ThrowRepository(BaseRepository):
    DB_MODEL = Throw
    MODEL_IN = ThrowIn
    MODEL_OUT = ThrowOut


def get_throw_repository(session: Session = Depends(get_db)):
    return ThrowRepository(db_session=session)
