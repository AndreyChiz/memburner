from fastapi import APIRouter

from config import settings
from .document import document_router
from .section import section_router
from .question import question_router


api_v1_router = APIRouter(prefix=settings.api.v1.prefix.root)

api_v1_router.include_router(
    router=document_router,
    prefix=settings.api.v1.prefix.document,
    tags=[settings.api.v1.tag.document],
)
api_v1_router.include_router(
    router=section_router,
    prefix=settings.api.v1.prefix.section,
    tags=[settings.api.v1.tag.section],
)
api_v1_router.include_router(
    router=question_router,
    prefix=settings.api.v1.prefix.question,
    tags=[settings.api.v1.tag.question],
)
