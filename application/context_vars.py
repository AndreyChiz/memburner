import contextvars
from config import settings

"just for logging, one common request_id"

request_id_var = contextvars.ContextVar(
    "request_id",
    default=settings.app_name,
)
