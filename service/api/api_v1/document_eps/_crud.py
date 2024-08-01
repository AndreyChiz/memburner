from typing import Sequence


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import Document

class DocumentCRUD():
    @staticmethod
    async def get_all_documents(session: AsyncSession)-> Sequence[Document]:
        stmt = select(Document).order_by(Document.id)
        result = await session.scalars(stmt)
        return result.all()