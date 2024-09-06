import uuid
import datetime


from sqlalchemy import (
    text,
    DateTime,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.dialects.postgresql import UUID as types_Uuid
from sqlalchemy.ext.declarative import declared_attr


class BaseMixin:
    __include_id__: bool = False
    __include_created_at__: bool = False
    __include_updated_at__: bool = False

    @declared_attr
    def id(cls) -> Mapped[uuid.UUID]:
        if cls.__include_id__:
            return mapped_column(
                types_Uuid(as_uuid=True),
                primary_key=True,
                server_default=text("gen_random_uuid()"),
            )

    @declared_attr
    def created_at(cls) -> Mapped[datetime.datetime | None]:
        if cls.__include_created_at__:
            return mapped_column(
                nullable=False,
                server_default=func.CURRENT_TIMESTAMP(),
                type_=DateTime(timezone=True),
            )

    @declared_attr
    def updated_at(cls) -> Mapped[datetime.datetime | None]:
        if cls.__include_updated_at__:
            return mapped_column(
                server_default=None,
                server_onupdate=func.CURRENT_TIMESTAMP(),
                type_=DateTime(timezone=True),
            )
