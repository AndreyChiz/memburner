from typing import Annotated
from fastapi import (
    Depends,
    APIRouter,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master
from config import settings

from core.database.models import Section
from ._schema import SectionRSP, SectionBase
from ._crud import SectionCRUD

section_router = APIRouter()


@section_router.get(
    "",
    response_model=list[SectionRSP],
)
async def get_sections(
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):
    sections = await SectionCRUD.get_all_sections(session)
    return sections


@section_router.post(
    "",
    response_model=SectionRSP,
)
async def create_section(
    new_section: SectionBase,
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):

    responce = await SectionCRUD.create_section(session=session, section=new_section)
    return responce
