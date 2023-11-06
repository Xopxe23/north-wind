from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings

sync_engine = create_engine(
    url=settings.DB_URL,
    echo=True,
)

session_maker = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    pass
