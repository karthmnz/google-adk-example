import os
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
import logging

AGENT_DIR = "."
SESSION_DB_URL = "sqlite:///./sessions.db"
ALLOWED_ORIGINS = ["http://0.0.0.0", "http://0.0.0.0:8888", "*"]

SERVE_WEB_INTERFACE = True

app: FastAPI = get_fast_api_app(
    agent_dir=AGENT_DIR,
    session_db_url=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/hello")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8888)), log_level="info", reload=True)
