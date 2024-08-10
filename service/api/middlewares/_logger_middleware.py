from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger
from fastapi import Request, Response
from datetime import datetime
import json

class LogRequestsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

        # Сбор информации о запросе
        request_info = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "client": str(request.client.host),
        }

        # Пытаемся извлечь тело запроса
        try:
            body = await request.json()
            request_info["body"] = body
        except Exception:
            request_info["body"] = "Не удалось декодировать тело запроса как JSON."

        # Логируем запрос
        logger.bind(request_id=request_id).info(
            f"Начало обработки: {json.dumps(request_info, ensure_ascii=False, indent=4)}"
        )

        # Выполняем основной запрос и получаем ответ
        response: Response = await call_next(request)

        # Сбор информации об ответе
        response_info = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
        }

        # Пытаемся извлечь тело ответа
        if response.media_type == "application/json":
            try:
                response_body = response.body.decode('utf-8')
                response_info["body"] = json.loads(response_body)
            except Exception:
                response_info["body"] = "Не удалось декодировать тело ответа как JSON."
        else:
            response_info["body"] = "Ответ не является JSON."

        # Логируем ответ
        logger.bind(request_id=request_id).info(
            f"Завершение обработки: {json.dumps(response_info, ensure_ascii=False, indent=4)}"
        )

        return response

