from pydantic import BaseModel


class ApiV1Prefix(BaseModel):
    root: str = "/v1"
    document: str = "/document"
    question: str = "/question"
    section: str = "/section"


class ApiV1Config(BaseModel):
    prefix: ApiV1Prefix = ApiV1Prefix()


class ApiConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Config = ApiV1Config()
