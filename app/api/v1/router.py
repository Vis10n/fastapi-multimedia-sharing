from fastapi import APIRouter

from app.api.v1.routes.posts import router as post_configuration_router

api_router: APIRouter = APIRouter(prefix="/v1")

api_router.include_router(post_configuration_router)
