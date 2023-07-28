from fastapi import FastAPI, Depends

from .auth.config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
from .database import User

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

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonymous"
