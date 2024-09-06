from typing import List, TYPE_CHECKING

import uuid
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ._base import Base

if TYPE_CHECKING:
    from ._section import Section


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
