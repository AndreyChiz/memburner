from typing import Sequence


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import Document
from ._schema import DocumentBase, DocumentRSP


class DocumentCRUD:
    @staticmethod
    async def get_all_documents(session: AsyncSession) -> Sequence[Document]:
        stmt = select(Document).order_by(Document.id)
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def create_document(session: AsyncSession, document: DocumentBase):
        document: Document = Document(**document.model_dump())
        session.add(document)
        await session.commit()
        # await session.refresh()
        return document
