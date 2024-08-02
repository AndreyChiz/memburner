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


class OpenApiConfig(BaseModel):
    title: str = "Examination servise API documentation"
    doc_version: str = "0.0.1"
    description: str = (
        "This API include the endpoints for operate the Documents,  Sections and Questions "
    )
    version: str = "3.1.0"


class ApiV1Config(BaseModel):
    prefix: ApiV1Prefix = ApiV1Prefix()
    tag: ApiTag = ApiTag()
    openapi: OpenApiConfig = OpenApiConfig(
        doc_version="0.0.2",
        version="3.0.0",
    )


class ApiConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Config = ApiV1Config()
