from typing import Sequence

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import Question
from ._schema import QuestionBase, QuestionRSP
from .._exceptions import QuestionAlreadyExistsException


class QuestionCRUD:
    @staticmethod
    async def get_all_questions(session: AsyncSession) -> Sequence[Question]:
        stmt = select(Question).order_by(Question.id)
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def create_question(session: AsyncSession, question: QuestionBase):
        question: Question = Question(**question.model_dump())
        session.add(question)
        try:
            await session.commit()
        except IntegrityError as e:
            raise QuestionAlreadyExistsException
                # await session.refresh()
        return question
