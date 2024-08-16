import uuid
from typing import Annotated


from pydantic import BaseModel, ConfigDict, constr


class DocumentBase(BaseModel):
    owner_user_id: uuid.UUID
    name: str
    code: Annotated[str, constr(min_length=5, max_length=100)]


class DocumentRSP(DocumentBase):
    id: uuid.UUID

    model_config = ConfigDict(title="Document response model schema ")
