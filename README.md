# Speech API Server using whisper

## Environment Variables
- UVICORN_HOST (default: 0.0.0.0)
- UVICORN_PORT (default: 8000)
- LOGGING_LEVEL (default: INFO)
- WHISPER_MODEL (default: base)


## API Document
http://{HOST}:{PORT}/docs


## Reference
- https://github.com/openai/whisper
- https://www.uvicorn.org/settings/
- https://fastapi.tiangolo.com/async/#very-technical-details
- https://fastapi.tiangolo.com/deployment/server-workers/#uvicorn-with-workers