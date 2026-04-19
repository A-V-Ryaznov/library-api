from fastapi import APIRouter

from .book import router as book_router
from .health import router as health_router
from .user import router as user_router

main_router = APIRouter()
main_router.include_router(health_router)
main_router.include_router(book_router)
main_router.include_router(user_router)


__all__ = ["main_router"]
