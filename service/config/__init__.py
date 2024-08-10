__all__ = "logger"

from pydantic_settings import BaseSettings, SettingsConfigDict


from ._api_config import ApiConfig
from ._run_config import RunConfig
from ._db_config import DatabaseConfig
from ._logger_config import logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(".env.template", ".env"),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
    )
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    database: DatabaseConfig


settings = Settings()
