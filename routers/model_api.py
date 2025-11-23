from typing import Annotated
from fastapi import APIRouter, Depends

from ai.speech_generator import SpeechGenerator
import ai.model_parameters
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
    print('Начало генерации речи')
    return SpeechResponse(speech=speech_generator.generate_speech(request, load_styles()))


@router.post("/set_model_settings")
async def set_model_settings(settings: ModelSettings):
    ai.model_parameters.do_sample = settings.do_sample
    ai.model_parameters.max_length = settings.max_length
    ai.model_parameters.max_new_tokens = settings.max_new_tokens
    ai.model_parameters.repetition_penalty = settings.repetition_penalty
    ai.model_parameters.temperature = settings.temperature
    ai.model_parameters.top_k = settings.top_k
    ai.model_parameters.top_p = settings.top_p
