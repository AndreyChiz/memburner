from fastapi import FastAPI


async def inspect_routes(app: FastAPI) -> None:
    for route in app.routes:
        if hasattr(route, "endpoint"):
            print(f"Путь: {route.path}")
            print(f"Имя: {route.name}")
            if hasattr(route, "response_model"):
                print(f"Модель ответа: {route.response_model}")
            
