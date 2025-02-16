from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import HttpClient
from app.routers import user, user_auth
from config import Config

config = Config()

@asynccontextmanager
async def lifespan(app: FastAPI):

    await HttpClient().start()
    yield  # after start
    await HttpClient().stop()


app = FastAPI(lifespan=lifespan)

origins = [
    config.BASE_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    user_auth.router,
    tags=["Auth"],
)
app.include_router(
    user.router,
    tags=["Users"],
)
