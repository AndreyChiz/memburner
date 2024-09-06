import uuid
from typing import Annotated


from pydantic import BaseModel, ConfigDict, constr


class SectionBase(BaseModel):

    name: str
    document_id: str
    section_id: uuid.UUID


class SectionRSP(SectionBase):
    id: uuid.UUID

    model_config = ConfigDict(title="Section response model schema ")
