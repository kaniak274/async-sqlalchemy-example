from typing import AsyncIterator

from sqlalchemy import select

from .database import get_session, Tutorial as TutorialDb
from .dto import Tutorial


async def create_tutorial(tutorial: Tutorial) -> Tutorial:
    async with get_session() as session:
        tutorial_db_instance = TutorialDb(
            name=tutorial.name,
        )
        session.add(tutorial_db_instance)
        await session.commit()
        await session.refresh(tutorial_db_instance)
        return tutorial_db_instance


async def list_tutorials() -> AsyncIterator[Tutorial]:
    async with get_session() as session:
        query = await session.execute(select(TutorialDb))
        tutorials_db = query.scalars().all()

        for tutorial_db in tutorials_db:
            yield Tutorial(tutorial_id=tutorial_db.tutorial_id, name=tutorial_db.name)
