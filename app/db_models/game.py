from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.db_models.base import BaseDBModel


class Game(BaseDBModel):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    first_user_name = Column(String(200), nullable=False)
    second_user_name = Column(String(200), nullable=False)
    turns = relationship("Turn", backref="game")

    @hybrid_property
    def turn_ids(self):
        return [item.id for item in self.turns]
