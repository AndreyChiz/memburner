from pydantic import BaseModel


class LoggerConfig(BaseModel):
    path: str
    file_name_perfix: str
    level: str
    rotation: str
    retention: str
    log_format: str
