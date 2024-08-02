from fastapi import APIRouter

from .api_v1 import api_v1_router
from .utils import inspect_routes

__all__ = inspect_routes


frst_api_router = APIRouter()

frst_api_router.include_router(api_v1_router)
