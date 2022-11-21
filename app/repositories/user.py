from fastapi import Depends
from sqlalchemy.orm import Session

from app.api_models.user import UserIn, UserOut
from app.exceptions.base import DbItemNotFoundError
from app.db.session import get_db
from app.db_models import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    DB_MODEL = User
    MODEL_IN = UserIn
    MODEL_OUT = UserOut

    def get_by_name(self, username: str):
        item = self.session.query(self.DB_MODEL).filter_by(username=username).first()
        if not item:
            raise DbItemNotFoundError(self.DB_MODEL, username)
        return self.convert(item)


def get_user_repository(session: Session = Depends(get_db)):
    return UserRepository(db_session=session)
