import uuid
from typing import Annotated


from pydantic import BaseModel, ConfigDict, constr, Field


class DocumentBase(BaseModel):
    owner_user_id: uuid.UUID
    name: str
    code: Annotated[str, constr(min_length=5, max_length=100)]


class DocumentRSP(DocumentBase):
    id: uuid.UUID
    owner_user_id: uuid.UUID = Field(exclude=True)
    model_config = ConfigDict(title="Document response model schema ")
