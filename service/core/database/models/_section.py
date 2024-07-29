import uuid
from typing import List, TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ._base import Base

if TYPE_CHECKING:
    from ._document import Document
    from ._question import Question


class Section(Base):
    """
    The :class:`Section` class within a document, containing related questions.

    :param name:
        The unique name of the section.
    :type name: str

    :param document_id:
        The UUID of the document to which this section belongs.
    :type document_id: uuid.UUID

    :ivar document:
        The document to which this section belongs.
    :vartype document: Document

    :ivar questions:
        The list of questions associated with this section.
    :vartype questions: list[Question]

    :seealso: additional blank fields in :paramref:`exam_service.models._base.Base` parameter.
    """

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    document_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("document.id"))

    document: Mapped["Document"] = relationship(back_populates="sections")
    questions: Mapped[List["Question"]] = relationship(back_populates="section")
