from fastapi import Request

from fastapi.responses import JSONResponse

from app.infrastructure.logger import logger


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
