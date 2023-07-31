from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from .auth.config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .operations.router import router as router_operations
from .background_tasks.router import router as router_background_tasks

app = FastAPI(
    title="trading app"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],

)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    router_operations,
    prefix="/operations",
    tags=["operations"]
)

app.include_router(
    router_background_tasks,
    prefix="/reports",
    tags=["background_tasks"]
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
