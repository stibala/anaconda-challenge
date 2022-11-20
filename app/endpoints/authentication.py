from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from starlette import status

from app.settings import Settings
from app.utils import authenticate_user, fake_users_db, create_access_token, User, get_current_active_user, Token

settings = Settings()

router = APIRouter(
    tags=["authentication"],
)


@cbv(router)
class Authentication:
    """Router for authentication"""

    @router.post("/token", response_model=Token)
    async def login_for_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
        """see documentation https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/"""
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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

    @router.get("/users/me/", response_model=User)
    async def read_users_me(self, current_user: User = Depends(get_current_active_user)):
        return current_user

    @router.get("/users/me/items/")
    async def read_own_items(self, current_user: User = Depends(get_current_active_user)):
        return [{"item_id": "Foo", "owner": current_user.username}]
