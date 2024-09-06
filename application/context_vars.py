import contextvars
from config import settings

request_id_var = contextvars.ContextVar(
    "request_id",
    default=settings.app_name,
)
