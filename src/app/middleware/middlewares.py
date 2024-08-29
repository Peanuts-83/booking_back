from urllib import response
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class PrefixMiddleware(BaseHTTPMiddleware):
    """
    check for & remove "/booking/api" at the begining of any request path
    """
    async def dispatch(self,request: Request, call_next):
        if not request.scope["path"].startswith("/booking/api/"):
            return JSONResponse(status_code=404, content={"detail": "Not found", "info": "path prefix missing"})
        request.scope["path"] = request.scope["path"][12:]
        response = await call_next(request)
        return response