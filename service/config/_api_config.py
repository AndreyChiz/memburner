from pydantic import BaseModel


class ApiV1Prefix(BaseModel):
    root: str = "/v1"
    document: str = "/document"
    section: str = "/section"
    question: str = "/question"


class ApiTag(BaseModel):
    document: str = "Document"
    section: str = "Section"
    question: str = "Question"


class ApiV1Config(BaseModel):
    prefix: ApiV1Prefix = ApiV1Prefix()
    tag: ApiTag = ApiTag()


class ApiConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Config = ApiV1Config()
