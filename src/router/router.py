from src.router.user_api_router import api_router
from fastapi import APIRouter


AllRouter = APIRouter()
# API路由
AllRouter.include_router(api_router)