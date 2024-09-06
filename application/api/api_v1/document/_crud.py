from typing import Sequence

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import Document
from ._schema import DocumentBase, DocumentRSP
from .._exceptions import DocumentAlreadyExistsException


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
        try:
            await session.commit()
        except IntegrityError as e:
            raise DocumentAlreadyExistsException
        return document
