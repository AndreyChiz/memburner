import uuid
from typing import Annotated


from pydantic import BaseModel, constr


class DocumentBase(BaseModel):
    owner: str
    name: str
    code: Annotated[str, constr(min_length=5, max_length=100)]


class DocumentRead(DocumentBase):
    id: uuid.UUID
