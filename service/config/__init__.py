from pydantic_settings import BaseSettings


from ._api_config import ApiConfig
from ._run_config import RunConfig

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    pass


settings = Settings()
