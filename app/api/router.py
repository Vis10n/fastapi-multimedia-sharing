from fastapi import APIRouter

from health import router as health_router
from .v1.router import api_router as api_v1_router

root_router = APIRouter()

# Include versioned APIs
root_router.include_router(health_router)
root_router.include_router(api_v1_router)
