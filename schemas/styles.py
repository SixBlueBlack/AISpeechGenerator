from pydantic import BaseModel


class SpeechStyle(BaseModel):
    name: str
    description: str
