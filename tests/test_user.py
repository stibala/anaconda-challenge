import pytest

from app.api_models.user import UserIn, UserOut, UserDBIn
from app.db_models import User
from app.repositories.user import UserRepository

USER_IN = UserIn(
    username="Adam",
    full_name="Adam Stibal",
    email="adam.stibal@gmail.com",
    password="hahaha",
)

USER_DB_IN = UserDBIn(
    username="Adam",
    full_name="Adam Stibal",
    email="adam.stibal@gmail.com",
    hashed_password="5u4325safdsa",
)


@pytest.fixture
def user_repository(session) -> UserRepository:
    return UserRepository(db_session=session)


@pytest.fixture
def user(user_repository) -> UserOut:
    return user_repository.create(USER_DB_IN)


def test_create(user_repository, session):
    assert len(session.query(User).all()) == 0
    user_repository.create(USER_DB_IN)
    items = session.query(User).all()
    assert len(items) == 1
    actual = items[0]
    assert USER_DB_IN == actual


def test_get(user, user_repository):
    actual = user_repository.get(1)
    assert actual == user


def test_remove(user, user_repository):
    assert len(user_repository.get_list()) == 1
    user_repository.delete(1)
    assert len(user_repository.get_list()) == 0
