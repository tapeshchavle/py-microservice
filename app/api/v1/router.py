from fastapi import APIRouter

from app.api.v1.items import router as items_router
from app.api.v1.users import router as users_router
from app.api.v1.java_integration import router as java_integration_router

# The main router that aggregates all endpoints for 'v1'
router = APIRouter()

# Register all individual resource routers here
router.include_router(items_router)
router.include_router(users_router)
router.include_router(java_integration_router)
