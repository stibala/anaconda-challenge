
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.api_models.game import GameIn, GameOut, GameDBIn
from app.api_models.user import UserOut
from app.repositories.game import get_game_repository, GameRepository
from app.repositories.user import UserRepository, get_user_repository
from app.settings import Settings
from app.utils import get_current_active_user

router = APIRouter(
    tags=["Game"],
)

settings = Settings()


@cbv(router)
class Game:

    repository: GameRepository = Depends(get_game_repository)
    current_user: UserOut = Depends(get_current_active_user)
    user_repository: UserRepository = Depends(get_user_repository)

    @router.post(
        path="/game",
        response_model=GameOut
    )
    def create_game(self, game: GameIn) -> GameOut:
        other_user_name = game.other_user_name or settings.computer_name
        # validates user exists
        self.user_repository.get_by_name(other_user_name)
        return self.repository.create(
            GameDBIn(first_user_name=self.current_user.username, second_user_name=other_user_name)
        )

    @router.get(
        path="/game/{game_id}",
        response_model=GameOut
    )
    def get_turn(self, game_id: int) -> GameOut:
        return self.repository.get(game_id)
