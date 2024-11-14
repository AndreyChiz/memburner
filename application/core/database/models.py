from typing import List

import uuid

from sqlalchemy import String, SmallInteger, ARRAY, UniqueConstraint, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import Base


from .base_model import Base


class Document(Base):
    __include_id__ = True
    __include_created_at__ = True
    __include_updated_at__ = True

    __table_args__ = (
        UniqueConstraint(
            "owner_user_id",
            "name",
            "code",
        ),
    )

    owner_user_id: Mapped[uuid.UUID] = mapped_column(unique=False)
    name: Mapped[str] = mapped_column(unique=False)
    code: Mapped[str | None] = mapped_column(String(100), unique=False)
    sections: Mapped[List["Section"]] = relationship(back_populates="document")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, code={self.code!r}, id={self.id})"

    def __repr__(self):
        return str(self)


class Section(Base):
    __include_id__ = True

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    document_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("document.id"))

    document: Mapped["Document"] = relationship(back_populates="sections")
    questions: Mapped[List["Question"]] = relationship(back_populates="section")


class Question(Base):
    __include_id__ = True

    quest_text: Mapped[str] = mapped_column(unique=True)
    answers: Mapped[list[str]] = mapped_column(ARRAY(String))
    section_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("section.id"))

    section: Mapped["Section"] = relationship(back_populates="questions")
