from datetime import timedelta
from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from starlette import status

from app.api_models.user import UserOut
from app.repositories.user import UserRepository, get_user_repository
from app.settings import Settings
from app.utils import create_access_token, Token, verify_password

settings = Settings()

router = APIRouter(
    tags=["authentication"],
)


@cbv(router)
class Authentication:
    """Router for authentication"""

    repository: UserRepository = Depends(get_user_repository)

    @router.post("/token", response_model=Token)
    async def login_for_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        """see documentation https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/"""
        user = self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def authenticate_user(self, username: str, password: str) -> Union[bool, UserOut]:
        user = self.repository.get_by_name(username)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
