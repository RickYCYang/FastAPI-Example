import logging
import os.path as path
import sys
from typing import List
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from core.logging import InterceptHandler

dotenv_path = path.abspath(path.join(__file__ ,"../../../.env"))
config = Config(dotenv_path)

API_PREFIX = "/api"
VERSION = "0.0.0"
JWT_TOKEN_PREFIX = "Token"  # noqa: S105
DEBUG: bool = config("DEBUG", cast=bool, default=False)
PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# uvicorn configuration
UVICORN_HOST: str = config("UVICORN_HOST", default="localhost")
UVICORN_PORT: int = config("UVICORN_PORT", cast=int, default=5000)
UVICORN_RELOAD: bool = config("UVICORN_RELOAD", cast=bool, default=False)
UVICORN_ACCESS_LOG: bool = config("UVICORN_ACCESS_LOG", cast=bool, default=False)
UVICORN_LOG_LEVEL: str = "debug" if DEBUG else "info"
