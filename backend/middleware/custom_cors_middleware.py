from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class CustomCORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        origin = request.headers.get('Origin')
        if origin:
            print(f"Origin: {origin}")
        else:
            print("No Origin header present.")
        # Establece los headers básicos de CORS
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'

        # Permite explícitamente ciertos headers, incluido Authorization
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Content-Type, Accept'

        # Permite el envío de credenciales como cookies y tokens de autenticación
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        # Maneja las solicitudes preflight para CORS
        if request.method == "OPTIONS":
            preflight_response = Response(status_code=200)
            preflight_response.headers.update({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Authorization, Origin, Content-Type, Accept',
                'Access-Control-Allow-Credentials': 'true'
            })
            return preflight_response

        return response
