from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import Config  # Assume you have a secret key set in settings.

config = Config()

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Do somthing here
        return response
