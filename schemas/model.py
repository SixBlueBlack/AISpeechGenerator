from pydantic import BaseModel
from typing import List, Optional


class SpeechRequest(BaseModel):
    topic: str
    duration_minutes: int
    style: str = "professional"
    key_points: Optional[List[str]] = None
    language: str = "ru"
    custom_instructions: Optional[str] = None


class SpeechResponse(BaseModel):
    speech: str


class ModelSettings(BaseModel):
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50
    max_length: int = 2048
    max_new_tokens: int = 2048
    repetition_penalty: float = 1.1
    do_sample: bool = True
