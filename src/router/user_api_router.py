from fastapi import APIRouter

from src.controller.user_api.user import router as user_router

api_router = APIRouter(prefix="/api", tags=["用户相关API"])

api_router.include_router(user_router)
