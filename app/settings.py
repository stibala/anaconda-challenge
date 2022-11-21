
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings"""

    database_uri: str
    data_path: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    algorithm: str
    jwt_secret_key: str
    jwt_refresh_secret_key: str
    database_uri: str
    computer_name: str


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"