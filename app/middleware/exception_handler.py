"""Exception handler module"""

from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exceptions.base import DbItemNotFoundError, TurnFinishedError, InvalidThrowUsernameError


def add_exception_handler(app: FastAPI):
    def __not_found(ex):
        return JSONResponse(status_code=404, content={"message": f"{ex}"})

    def __unprocessable_entity(ex):
        return JSONResponse(status_code=422, content={"message": str(ex)})

    @app.exception_handler(IntegrityError)
    async def integrity_error_exception_handler(request: Request, exc: IntegrityError):
        return __unprocessable_entity(exc.orig)

    @app.exception_handler(DbItemNotFoundError)
    async def db_item_not_found_exception_handler(request: Request, exc: DbItemNotFoundError):
        return __not_found(exc)

    @app.exception_handler(TurnFinishedError)
    async def turn_finished_exception_handler(request: Request, exc: TurnFinishedError):
        return __unprocessable_entity(exc)

    @app.exception_handler(InvalidThrowUsernameError)
    async def invalid_throw_username_exception_handler(request: Request, exc: InvalidThrowUsernameError):
        return __unprocessable_entity(exc)
