from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master

from . import router
from ._schema import DocumentRead
from ._crud import DocumentCRUD


@router.get("", response_model=list[DocumentRead])
async def get_documents(
    session: AsyncSession = Depends(db_master.session_getter),
):
    documents = await DocumentCRUD.get_all_documents(session=session)
    return documents
