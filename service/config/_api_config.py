from pydantic import BaseModel


class ApiConfig(BaseModel):
    prefix: str = "/api"
