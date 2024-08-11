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

        # Логируем начало обработки
        logger.bind(request_id=request_id).info(
            f"Начало обработки: {json.dumps(request_info, ensure_ascii=False, indent=4)}"
        )

        # Выполняем основной запрос и перехватываем ответ
        response = await call_next(request)

        # Чтение тела ответа
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        # Запись тела в response обратно
        response = Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),  # Сохраняем все заголовки ответа
            media_type=response.media_type,
        )

        # Сбор информации об ответе
        response_info = {
            "status_code": response.status_code,
            "headers": dict(response.headers),  # Добавляем все заголовки ответа
        }

        # Логируем тело ответа, если оно JSON
        if response.media_type == "application/json":
            try:
                # Попытка декодировать JSON тело ответа
                decoded_body = json.loads(response_body)
                response_info["body"] = decoded_body
            except json.JSONDecodeError:
                response_info["body"] = "Ответ содержит некорректный JSON."
        else:
            response_info["body"] = (
                response_body.decode("utf-8") if response_body else "Пустое тело ответа"
            )

        # Логируем завершение обработки
        logger.bind(request_id=request_id).info(
            f"Завершение обработки: {json.dumps(response_info, ensure_ascii=False, indent=4)}"
        )
        if response.status_code != 200:
            logger.bind(request_id=request_id).error(
                "\n" 
                f"ERROR_REQUEST: {json.dumps(request_info, ensure_ascii=False, indent=4)}"
                f"ERROR_RESPONSE: {json.dumps(response_info, ensure_ascii=False, indent=4)}"
            )
        return response

