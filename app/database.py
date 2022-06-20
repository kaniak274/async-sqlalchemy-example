import os

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

engine = create_async_engine(
    os.environ["DB_URL"],
    echo=True,
    future=True,
)

Base = declarative_base()


class Tutorial(Base):
    __tablename__ = "tutorials"

    tutorial_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
