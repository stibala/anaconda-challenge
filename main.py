from fastapi import FastAPI

from app.endpoints.health import router as health_router
from app.endpoints.authentication import router as authentication_router
from app.settings import Settings
from app.middleware.exception_handler import add_exception_handler

settings = Settings()
app = FastAPI(title="Rock Paper Scissors", version="1.0.0")

add_exception_handler(app)

app.include_router(health_router)
app.include_router(authentication_router)
