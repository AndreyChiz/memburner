from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class LoggerConfig(BaseModel):
    path: str
    file_name_perfix: str
    level: str
    rotation: str
    retention: str
    log_format: str
    compression: str


class OpenApiConfig(BaseModel):
    title: str = "Examination servise API documentation"
    doc_version: str = "0.0.1"
    description: str = (
        "This API include the endpoints for operate the Documents,  Sections and Questions "
    )
    version: str = "3.1.0"


class ApiV1Config(BaseModel):
    class ApiPrefix(BaseModel):
        root: str = "/v1"
        document: str = "/document"
        section: str = "/section"
        question: str = "/question"

    class ApiTag(BaseModel):
        document: str = "Document"
        section: str = "Section"
        question: str = "Question"

    prefix: "ApiPrefix" = ApiPrefix()
    tag: "ApiTag" = ApiTag()
    openapi: OpenApiConfig = OpenApiConfig(
        doc_version="0.0.2",
        version="3.0.0",
    )


class ApiConfig(BaseModel):

    prefix: str = "/api"
    v1: ApiV1Config = ApiV1Config()


class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = 5433
    name: str
    user: str
    password: str

    # url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    app_name: str
    model_config = SettingsConfigDict(
        case_sensitive=False,
        # env_file=(".env.template", ".env"),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
    )
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    database: DatabaseConfig
    logger: LoggerConfig


settings = Settings()
