import json
import time
import logging
from main import app 
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import StreamingResponse
import ast








# class LoggingMiddleware(BaseHTTPMiddleware):
#     '''Middleware Class to log user activity'''
#     async def dispatch(self, request: Request, call_next) -> Response:
#         start_time = time.time()
#         try:
#             body = await request.json()
#         except json.decoder.JSONDecodeError:
#             body = ""
#         log = {
#             "endpoint": request.url.path,
#             "browser": request.headers["sec-ch-ua"] if "sec-ch-ua" in request.headers else "",
#             "referer": request.headers["referer"] if "referer" in request.headers else "",
#             "payload": body
#         }
#         response = await call_next(request)

#         if "authorization" in request.headers:
#             try:
#                 log["user"] = request.state.user
#             except Exception:
#                 log["user"] = ""
#         log["response"] = response.status_code
#         process_time = time.time() - start_time
#         log["took"] = str(process_time)
#         response.headers["X-Process-Time"] = str(process_time)
#         logging.info(json.dumps(log))
        

#         return response
