from typing import List, TYPE_CHECKING

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ._base import Base

if TYPE_CHECKING:
    from .section import Section


class Document(Base):
    """The :class:`Document` class stores information about the name and code of the document for which the tests are compiled.
    Including its unique name, code, and associated sections.

    :param name:
     The name of the document is unique. It may be the title of a book or the name of a standard, etc
    :type name:
     str

    :param code:
     Document code or designation, such as a book's "ISBN..." or standard designation such as "ISO..."
    :type name:
     str

    :ivar sections:
    The list of sections that the document contains
    :vartype List[Section]

    :seealso: additional blank fields in :paramref:`exam_service.models._base.Base` parameter.

    """

    __table_args__ = (
        UniqueConstraint("owner", "name", "code", name="document_owner_name_code_key"),
    )

    owner: Mapped[str] = mapped_column(unique=False)
    name: Mapped[str] = mapped_column(unique=False)
    code: Mapped[str | None] = mapped_column(String(100), unique=False)
    sections: Mapped[List["Section"]] = relationship(back_populates="document")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, code={self.code!r}, id={self.id})"

    def __repr__(self):
        return str(self)
