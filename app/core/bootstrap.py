import logging

from fastapi import FastAPI
from app.api.router import root_router

from data.db import create_db_and_tables
from contextlib import asynccontextmanager

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


def bootstrap() -> FastAPI:
    app = create_app()
    return app


def create_app() -> FastAPI:
    log.info("Starting app...")

    app = FastAPI(lifespan=lifespan)
    app.include_router(root_router)

    return app
