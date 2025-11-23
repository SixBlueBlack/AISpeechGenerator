from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from ai.speech_generator import SpeechGenerator
from dependencies import get_speech_generator
from schemas.model import (
    SpeechRequest, SpeechResponse, ModelSettings
)
from utils import load_styles

router = APIRouter()


@router.post("/generate_speech", response_model=SpeechResponse)
async def generate_speech(
    request: SpeechRequest,
    speech_generator: Annotated[SpeechGenerator, Depends(get_speech_generator)]
    ):
    return speech_generator.generate_speech(request, load_styles())


@router.post("/set_model_settings")
async def set_model_settings(settings: ModelSettings):
    raise HTTPException(status_code=501)
