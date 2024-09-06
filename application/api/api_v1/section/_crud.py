from typing import Sequence
import uuid

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import Section
from ._schema import SectionBase, SectionRSP
from .._exceptions import SectionAlreadyExistsException


class SectionCRUD:
    @staticmethod
    async def get_all_sections(
        session: AsyncSession, document_id: uuid.UUID
    ) -> Sequence[Section]:

        # TODO: добавить пагинацию, в запросе схема DocumentRSP, очереднсоть выборки id,code,name

        stmt = (
            select(Section)
            .where(Section.document_id == document_id)
            .order_by(Section.id)
        )
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def create_section(session: AsyncSession, section: SectionBase):
        section: Section = Section(**section.model_dump())
        session.add(section)
        try:
            await session.commit()
        except IntegrityError as e:
            raise SectionAlreadyExistsException
            # await session.refresh()
        return section
