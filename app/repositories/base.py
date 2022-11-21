"""Base repository module"""
from typing import TypeVar, Generic, List

from sqlalchemy.orm import Session

from app.api_models.base import BaseAPIModel
from app.db_models.base import BaseDBModel
from app.exceptions.base import DbItemNotFoundError

MODEL_IN_TYPE = TypeVar("MODEL_IN_TYPE", bound=BaseAPIModel)
DB_MODEL_TYPE = TypeVar("DB_MODEL_TYPE", bound=BaseDBModel)
MODEL_OUT_TYPE = TypeVar("MODEL_OUT_TYPE", bound=BaseAPIModel)


class BaseRepository(Generic[MODEL_IN_TYPE, DB_MODEL_TYPE, MODEL_OUT_TYPE]):
    """
    BaseRepository
    All class variables need to be set in derived classes
    """
    DB_MODEL: DB_MODEL_TYPE
    MODEL_IN: MODEL_IN_TYPE
    MODEL_OUT: MODEL_OUT_TYPE

    def __init__(self, db_session: Session):
        self.session = db_session

    def _get(self, identifier: int) -> DB_MODEL_TYPE:
        """gets an item from DB"""
        item = self.session.query(self.DB_MODEL).get(identifier)
        if not item:
            raise DbItemNotFoundError(self.DB_MODEL, identifier)
        return item

    def create(self, model_in: MODEL_IN_TYPE) -> MODEL_OUT_TYPE:
        """creates an item on database"""
        new_item = self.DB_MODEL(**model_in.dict())
        with self.session.begin_nested():
            self.session.add(new_item)

        return self.convert(new_item)

    def delete(self, identifier: int) -> MODEL_OUT_TYPE:
        """deletes an object from DB"""
        item = self._get(identifier)
        with self.session.begin_nested():
            self.session.delete(item)

        return self.convert(item)

    def get(self, identifier: int) -> MODEL_OUT_TYPE:
        """returns an object from DB"""
        return self.convert(self._get(identifier))

    def get_list(self) -> List[MODEL_OUT_TYPE]:
        """lists all objects from DB"""
        q = self.session.query(self.DB_MODEL)
        return [self.convert(item) for item in q.all()]

    def convert(self, model_in: DB_MODEL_TYPE) -> MODEL_OUT_TYPE:
        return self.MODEL_OUT.from_orm(model_in)
