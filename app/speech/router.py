import whisper
from fastapi import APIRouter, Request
from .config import WHISPER_MODEL
import logging
from pydantic import BaseModel, Field
import base64
import librosa
import io
import threading

class SpeechRequest(BaseModel):
    audio: str = Field(..., description="A base64-encoded string. Value: wav, mp3, m4a, webm, mp4, mpga, mpeg")
    language: str = Field(..., description="Translation supports only English. Value: en, ko, ja, zh")

class SpeechResponse(BaseModel):
    text: str


model = whisper.load_model(WHISPER_MODEL)
router = APIRouter()


@router.post("/transcription", tags=["Speech"], summary="Transcribe audio")
@router.post("/translation", tags=["Speech"], summary="Translate audio")
async def transcription(request: Request, speech: SpeechRequest) -> SpeechResponse:
    logging.info(f"transcription received... thread({threading.get_ident()})")

    # Checking Task
    task = request.url.path.split("/")[-1]
    if task == "transcription":
        task = "transciribe"
    else:
        task = "translate"

    # Decoding
    audio_bytes = base64.b64decode(speech.audio)
    bytesIO = io.BytesIO(audio_bytes)
    ndarray, _ = librosa.load(bytesIO)

    # Transcribing
    options = dict(task=task, language=speech.language, fp16=False)
    result = model.transcribe(ndarray, **options)

    return SpeechResponse(text=result["text"])
