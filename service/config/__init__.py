from pydantic_settings import BaseSettings, SettingsConfigDict


from ._api_config import ApiConfig
from ._run_config import RunConfig
from ._db_config import DatabaseConfig
from ._logger_config import LoggerConfig


class Settings(BaseSettings):
    app_name: str
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(".env.template", ".env"),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
    )
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    database: DatabaseConfig
    logger: LoggerConfig


settings = Settings()


# print(settings.model_dump_json(indent=2))
