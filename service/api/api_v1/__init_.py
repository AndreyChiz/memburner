from fastapi import APIRouter

from config import settings
from document_eps import router as user_router

router = APIRouter(perfix=settings.api.v1.prefix)
