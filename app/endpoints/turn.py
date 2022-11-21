from random import choice

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.api_models.throw import ThrowDBIn
from app.api_models.turn import TurnOut, TurnIn
from app.api_models.user import UserOut
from app.db_models.throw import Symbol
from app.repositories.game import get_game_repository, GameRepository
from app.repositories.throw import get_throw_repository, ThrowRepository
from app.repositories.turn import TurnRepository, get_turn_repository
from app.settings import Settings
from app.utils import get_current_active_user

router = APIRouter(
    tags=["Turn"],
)

settings = Settings()


@cbv(router)
class Turn:

    repository: TurnRepository = Depends(get_turn_repository)
    game_repository: GameRepository = Depends(get_game_repository)
    throw_repository: ThrowRepository = Depends(get_throw_repository)
    current_user: UserOut = Depends(get_current_active_user)

    @router.post(
        path="/game/{game_id}/turn",
        response_model=TurnOut
    )
    def create_turn(self, game_id: int) -> TurnOut:
        # validates the game exists
        game = self.game_repository.get(game_id)
        turn = self.repository.create(TurnIn(game_id=game_id))
        if settings.computer_name in [game.first_user_name, game.second_user_name]:
            throw = ThrowDBIn(turn_id=turn.id, username=settings.computer_name, value=choice(list(Symbol)).value)
            self.throw_repository.create(throw)
        return self.repository.get(turn.id)

    @router.get(
        path="/turn/{turn_id}",
        response_model=TurnOut
    )
    def get_turn(self, turn_id: int) -> TurnOut:
        return self.repository.get(turn_id)
