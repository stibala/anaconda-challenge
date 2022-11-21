from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from app.api_models.user import UserOut, UserIn, UserDBIn
from app.repositories.user import UserRepository, get_user_repository
from app.settings import Settings
from app.utils import get_password_hash, get_current_active_user

settings = Settings()

router = APIRouter(
    tags=["user"],
)


@cbv(router)
class User:
    """Router for authentication"""
    repository: UserRepository = Depends(get_user_repository)

    @router.get("/user/me/", response_model=UserOut, response_model_exclude={"hashed_password"})
    async def read_users_me(self, current_user: UserOut = Depends(get_current_active_user)):
        return current_user

    @router.post("/users/signin", response_model=UserOut, response_model_exclude={"hashed_password"})
    async def sign_in(self, user: UserIn):
        data = dict(user)
        del(data["password"])
        data["hashed_password"] = get_password_hash(user.password)
        return self.repository.create(UserDBIn(**data))
