from app.api_models.base import BaseAPIModel


class User(BaseAPIModel):
    """User class"""
    username: str
    full_name: str
    email: str


class UserIn(User):
    """User in class"""
    password: str


class UserDBIn(User):
    hashed_password: str


class UserOut(User):
    """User out class"""
    id: int
    disabled: bool
    hashed_password: str

    class Config:
        orm_mode = True
