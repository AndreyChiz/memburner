from pydantic_settings import BaseSettings, SettingsConfigDict


from ._api_config import ApiConfig
from ._run_config import RunConfig
from ._db_config import DatabaseConfig

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__"
    )
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    database: DatabaseConfig 


settings = Settings()
