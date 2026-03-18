from sqlalchemy.ext.asyncio import create_async_engine

from config import settings


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False
)
