import os
import logging

UVICORN_HOST = os.environ.get("UVICORN_HOST", "0.0.0.0")
UVICORN_PORT = int(os.environ.get("UVICORN_PORT", 8000))
LOGGING_LEVEL = logging._nameToLevel[os.environ.get("LOGGING_LEVEL", "INFO")]
