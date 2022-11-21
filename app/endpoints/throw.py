from random import choice

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.api_models.throw import ThrowIn, ThrowOut, ThrowDBIn
from app.api_models.user import UserOut
from app.db_models.throw import Symbol
from app.exceptions.base import TurnFinishedError, InvalidThrowUsernameError
from app.repositories.throw import ThrowRepository, get_throw_repository
from app.repositories.turn import get_turn_repository, TurnRepository
from app.repositories.game import get_game_repository, GameRepository
from app.utils import get_current_active_user

router = APIRouter(
    tags=["Throw"],
)


@cbv(router)
class Throw:

    repository: ThrowRepository = Depends(get_throw_repository)
    turn_repository: TurnRepository = Depends(get_turn_repository)
    game_repository: GameRepository = Depends(get_game_repository)
    current_user: UserOut = Depends(get_current_active_user)

    @router.post(
        path="/throw",
        response_model=ThrowOut
    )
    def create_throw(self, throw: ThrowIn) -> ThrowOut:
        if throw.value is None:
            throw.value = choice(list(Symbol)).value
        turn = self.turn_repository._get(throw.turn_id)
        allowed_names = list(
                {turn.game.first_user_name, turn.game.second_user_name} - {item.username for item in turn.throws}
        )
        if turn.finished:
            raise TurnFinishedError(turn.id)
        if self.current_user.username not in allowed_names:
            raise InvalidThrowUsernameError(allowed_names)
        return self.repository.create(
            ThrowDBIn(username=self.current_user.username, value=throw.value, turn_id=throw.turn_id)
        )
