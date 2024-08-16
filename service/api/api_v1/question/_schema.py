import uuid
from typing import Annotated


from pydantic import BaseModel, ConfigDict, constr


class QuestionBase(BaseModel):

    quest_text: str
    answers: list[str]
    section_id: uuid.UUID
    number_in_chapter: int
    code: Annotated[str, constr(min_length=5, max_length=100)]


class QuestionRSP(QuestionBase):
    id: uuid.UUID

    model_config = ConfigDict(title="Question response model schema ")
