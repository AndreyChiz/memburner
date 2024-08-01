from fastapi import (
    Depends,
    APIRouter,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master

from ._schema import DocumentRead
from ._crud import DocumentCRUD

document_router = APIRouter(tags=["Document"])


@document_router.get("/", response_model=list[DocumentRead])
async def get_documents(
    session: AsyncSession = Depends(db_master.session_getter),
):
    documents = await DocumentCRUD.get_all_documents(session=session)
    return documents
