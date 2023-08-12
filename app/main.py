from fastapi import FastAPI
import uvicorn
import logging
from config import ( LOGGING_LEVEL, UVICORN_HOST, UVICORN_PORT )
from speech.router import router as speech_router


app = FastAPI(
    title='Whisper Server',
    description='Speech model server using Whisper',
    docs_url="/docs",
    redoc_url=None
)
app.include_router(speech_router, prefix="/speech")


if __name__ == '__main__':
    logging.basicConfig(level=LOGGING_LEVEL)
    uvicorn.run("main:app", host=UVICORN_HOST, port=UVICORN_PORT, log_level="info")
