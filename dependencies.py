from ai.speech_generator import SpeechGenerator

_speech_generator = None

async def get_speech_generator() -> SpeechGenerator:
    """Глобальная зависимость SpeechGenerator."""
    if _speech_generator is None:
        raise RuntimeError("SpeechGenerator не инициализирован")
    return _speech_generator

def init_speech_generator():
    """Инициализация SpeechGenerator при старте приложения"""
    print('Начало загрузки модели...')
    global _speech_generator
    _speech_generator = SpeechGenerator()
    _speech_generator.load_model() 
    print('Модель загружена')
