from pydantic_settings import BaseSettings


from ._api_config import ApiConfig
from ._run_config import RunConfig
from ._db_config import DatabaseConfig

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    database: DatabaseConfig 


settings = Settings()
