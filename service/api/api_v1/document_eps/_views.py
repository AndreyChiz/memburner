from typing import Annotated
from fastapi import (
    Depends,
    APIRouter,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master
from config import settings

from core.database.models import Document
from ._schema import DocumentRSP, DocumentBase
from ._crud import DocumentCRUD

document_router = APIRouter(
    prefix=settings.api.v1.prefix.document,
    tags=[settings.api.v1.tag.document],
)


@document_router.get(
    "",
    response_model=list[DocumentRSP],
)
async def get_documents(
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):
    documents = await DocumentCRUD.get_all_documents(session)
    return documents


@document_router.post(
    "",
    response_model=DocumentRSP,
)
async def create_document(
    new_document: DocumentBase,
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):
   
    responce = await DocumentCRUD.create_document(
        session=session, document=new_document
    )
    return responce
