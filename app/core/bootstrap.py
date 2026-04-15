import logging

from fastapi import FastAPI
from app.api.router import root_router

log = logging.getLogger(__name__)


def bootstrap() -> FastAPI:
    app = create_app()
    return app


def create_app() -> FastAPI:
    log.info("Starting app...")

    app = FastAPI()
    app.include_router(root_router)

    return app
