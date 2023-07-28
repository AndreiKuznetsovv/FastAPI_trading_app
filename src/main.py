from fastapi import FastAPI

from .auth.config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .operations.router import router as router_operations

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
