import uuid
from typing import List, TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ._base import Base

if TYPE_CHECKING:
    from ._document import Document
    from ._question import Question


class Section(Base):
    __include_id__ = True

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    document_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("document.id"))

    document: Mapped["Document"] = relationship(back_populates="sections")
    questions: Mapped[List["Question"]] = relationship(back_populates="section")
