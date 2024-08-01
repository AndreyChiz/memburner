from fastapi import APIRouter

from config import settings
from .document_eps import document_router




api_v1_router = APIRouter(prefix=settings.api.v1.prefix.root)

api_v1_router.include_router(router=document_router,)



