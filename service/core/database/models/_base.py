import uuid
import datetime

from sqlalchemy import text, event, DateTime, func, MetaData
from sqlalchemy.dialects.postgresql import UUID as types_Uuid
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from typing import Any, Annotated
from src.config import settings

idpk = Annotated[
    uuid.UUID, mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
]


class Base(DeclarativeBase):
    """
    The :class:`Base` class serves as the base class for all database models.

    :param id:
        The primary key of the model.
        :seealso: `exam_service.models._base.idpk` for type of the all PrimaryKeys
    :type id: idpk

    :param created_at:
        The timestamp when the instance was created.
    :type created_at: datetime.datetime

    :param updated_at:
        The timestamp when the instance was last updated.
    :type updated_at: datetime.datetime | None

    """

    __abstract__ = True

    metadata = MetaData(naming_convention=settings.DATABASE_NAMING_CONVENTION)

    id: Mapped[idpk]
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False,
        server_default=func.CURRENT_TIMESTAMP(),
        type_=DateTime(timezone=True),
    )
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        server_default=None,
        server_onupdate=func.CURRENT_TIMESTAMP(),
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self) -> str:
        values = ", ".join(
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        return f"{self.__class__.__name__}({values})"

    def to_dict(self) -> dict[str, Any]:
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        }

    def to_json(self) -> str:
        import json

        return json.dumps(self.to_dict(), default=str)


@event.listens_for(Base, "before_update")
def receive_before_update(mapper, connection, target):
    print(f"Updating {target.__tablename__}: {target}")


@event.listens_for(Base, "before_insert")
def receive_before_insert(mapper, connection, target):
    print(f"Inserting into {target.__tablename__}: {target}")
