from typing import Annotated
from fastapi import (
    Depends,
    APIRouter,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master
from config import settings

from ._schema import DocumentRead
from ._crud import DocumentCRUD

document_router = APIRouter(
    prefix=settings.api.v1.prefix.document,
    tags=[settings.api.v1.tag.document],
       
)


@document_router.get(path="", response_model=list[DocumentRead], )
async def get_documents(
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):
    documents = await DocumentCRUD.get_all_documents(session)
    return documents

