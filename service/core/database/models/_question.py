import uuid
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, SmallInteger
from sqlalchemy.types import String, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base

if TYPE_CHECKING:
    from ._section import Section


class Question(Base):
    __include_id__ = True

    quest_text: Mapped[str] = mapped_column(unique=True)
    answers: Mapped[list[str]] = mapped_column(ARRAY(String))
    section_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("section.id"))
    number_in_chapter: Mapped[int] = mapped_column(SmallInteger)

    section: Mapped["Section"] = relationship(back_populates="questions")
