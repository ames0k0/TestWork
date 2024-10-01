from fastapi import APIRouter

from .tasks import router as tasks

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
