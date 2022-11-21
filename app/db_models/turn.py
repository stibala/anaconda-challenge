from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.db_models.base import BaseDBModel
from app.db_models.throw import Symbol

win_map = {
    Symbol.rock: Symbol.scissors,
    Symbol.paper: Symbol.rock,
    Symbol.scissors: Symbol.paper,
}


class Turn(BaseDBModel):
    __tablename__ = "turn"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("game.id"))
    throws = relationship("Throw", backref="turn")

    @hybrid_property
    def finished(self):
        return len(self.throws) >= 2

    @hybrid_property
    def winner(self):
        if not self.finished:
            return None
        if self.throws[0].value == self.throws[1].value:
            return None
        if self.throws[1].value == win_map[self.throws[0].value]:
            return self.throws[0].username
        return self.throws[1].username
