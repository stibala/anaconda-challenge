from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as SQLAlchemySession

from app.settings import Settings

settings = Settings()

engine = create_engine(settings.database_uri, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[SQLAlchemySession, None, None]:
    session = Session()
    try:
        yield session
    finally:
        session.close()
