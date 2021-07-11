import uvicorn

from typing import Optional
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from api.errors.http_error import http_error_handler
from api.errors.validation_error import http422_error_handler
from api.routes.api import router 
from core.config import (
        ALLOWED_HOSTS,
        API_PREFIX,
        DEBUG,
        PROJECT_NAME,
        VERSION,
        UVICORN_HOST,
        UVICORN_PORT,
        UVICORN_RELOAD,
        UVICORN_ACCESS_LOG,
        UVICORN_LOG_LEVEL,
    )

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    # Middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Exceptions
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    # Router
    application.include_router(router, prefix=API_PREFIX)

    return application


app = get_application()


if __name__ == "__main__":
    # Run app with uvicorn with port and host specified. Host needed for docker port mapping
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=UVICORN_RELOAD, access_log=UVICORN_ACCESS_LOG, log_level=UVICORN_LOG_LEVEL)
