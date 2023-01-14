from fastapi import FastAPI
from src.users.views import router as users_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router, prefix="/users", tags=["users"])

    return app


app = create_app()
