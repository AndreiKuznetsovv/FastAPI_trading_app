import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from src import metadata
from src.config import settings
from src.database import get_async_session
from src.main import app

engine_test = create_async_engine(settings.DB_URL, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


# SETUP DB
@pytest.fixture(autouse=True, scope="session")
async def setup_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all())
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all())


# SETUP EVENT LOOP
@pytest.fixture(scope="session")
def event_loop(request):
    """Create the instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


# SETUP ASYNC CLIENT (ac)
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
