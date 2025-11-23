from fastapi import APIRouter, HTTPException

from schemas.model import (
    SpeechRequest, SpeechResponse, ModelSettings
)

router = APIRouter()


@router.post("/generate_speech", response_model=SpeechResponse)
async def generate_speech(request: SpeechRequest):
    raise HTTPException(status_code=501)


@router.post("/set_model_settings")
async def set_model_settings(settings: ModelSettings):
    raise HTTPException(status_code=501)
