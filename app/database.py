import os
from contextlib import asynccontextmanager

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

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


def async_session_generator():
    return sessionmaker(
        engine, class_=AsyncSession
    )


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
