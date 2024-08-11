# app/logging_config.py

from loguru import logger
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import sys
import os


# sentry_logging = LoggingIntegration(
#     level="INFO",  # Уровень логирования для отправки в Sentry
#     event_level="ERROR",  # Уровень логирования для создания события в Sentry
# )

# sentry_sdk.init(
#     dsn="your_sentry_dsn",  # Ваш DSN Sentry
#     integrations=[sentry_logging],
#     traces_sample_rate=1.0,  # Настройка выборки трассировок
# )

logger.remove()


log_path = "logs"
os.makedirs(log_path, exist_ok=True)

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {extra} | {message} |",
    level="INFO",
    colorize=True,

)
logger.add(
    os.path.join(log_path, "app_{time:YYYY-MM-DD}.log"),
    rotation="500 MB",  # Ротация по размеру
    retention="10 days",  # Удаление логов старше 10 дней
    compression="zip",  # Архивирование логов
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {extra} | {message} | ",
    level="ERROR",
    enqueue=True,  # Асинхронная запись в файл
    colorize=True,
)

# logger.add(lambda msg: sentry_sdk.capture_message(msg), level="ERROR")
