from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger

class UpstreamError(RuntimeError):
    def __init__(self, provider: str, status: int, detail: str = "Upstream error"):
        self.provider = provider
        self.status = status
        super().__init__(detail)

async def upstream_error_handler(request: Request, exc: UpstreamError):
    logger.error(f"Upstream {exc.provider} failed with {exc.status} on {request.url}")
    return JSONResponse(status_code=502, content={"error": "upstream_error", "provider": exc.provider})
