"""Exception handler module"""

from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.exceptions.base import DbItemNotFoundError


def add_exception_handler(app: FastAPI):
    def __not_found(ex):
        return JSONResponse(status_code=404, content={"message": f"{ex}"})

    def __unprocessable_entity(ex):
        return JSONResponse(status_code=422, content={"message": str(ex)})

    def __forbidden():
        return JSONResponse(status_code=403, content={"detail": "forbidden"})

    @app.exception_handler(IntegrityError)
    async def integrity_error_exception_handler(request: Request, exc: IntegrityError):
        return __unprocessable_entity(exc.orig)

    @app.exception_handler(DbItemNotFoundError)
    async def db_item_not_found_exception_handler(request: Request, exc: DbItemNotFoundError):
        return __not_found(exc.orig)
