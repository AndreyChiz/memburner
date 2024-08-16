from typing import Annotated
from fastapi import (
    Depends,
    APIRouter,
)

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_master
from config import settings

from core.database.models import Question
from ._schema import QuestionRSP, QuestionBase
from ._crud import QuestionCRUD

question_router = APIRouter()


@question_router.get(
    "",
    response_model=list[QuestionRSP],
)
async def get_questions(
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):
    questions = await QuestionCRUD.get_all_questions(session)
    return questions


@question_router.post(
    "",
    response_model=QuestionRSP,
)
async def create_question(
    new_question: QuestionBase,
    session: Annotated[AsyncSession, Depends(db_master.session_getter)],
):

    responce = await QuestionCRUD.create_question(
        session=session, question=new_question
    )
    return responce
