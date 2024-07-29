import uuid
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.types import String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base

if TYPE_CHECKING:
    from ._section import Section


class Question(Base):
    """
    The :class:`Question` class represents a single question that belongs to
    a specific section of a document.

    :param question_text:
        The text of the question.
    :type question_text: str

    :param answers:
        The list of possible answers to the question.
    :type answers: list[str]

    :param section_id:
        The UUID of the section to which this question belongs.
    :type section_id: uuid.UUID

    :param number_in_chapter:
        The sequential number of the question within its section.
    :type number_in_chapter: int

    :ivar section:
        The section to which this question belongs.
    :vartype section: Section

    :seealso: additional blank fields in :paramref:`exam_service.models._base.Base` parameter.
    """

    quest_text: Mapped[str] = mapped_column(unique=True)
    answers: Mapped[list[str]] = mapped_column(ARRAY(String))
    section_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("section.id"))
    number_in_chapter: Mapped[int] = mapped_column(SmallInteger)

    section: Mapped["Section"] = relationship(back_populates="questions")
