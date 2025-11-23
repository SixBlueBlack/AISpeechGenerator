from fastapi import APIRouter, HTTPException
from typing import List

from schemas.styles import SpeechStyle
from utils import load_styles, save_styles

router = APIRouter()


@router.post("")
async def set_styles(styles_list: List[SpeechStyle]):
    """Добавляет новые стили выступлений."""
    styles = load_styles()
    added_styles = []
    for style in styles_list:
        if style.name in styles:
            raise HTTPException(status_code=400, detail=f"Стиль с именем '{style.name}' уже существует")
        styles[style.name] = style.description
        added_styles.append(style.dict())
    save_styles(styles)
    return {"message": "Стили добавлены", "styles": added_styles}


@router.get("")
async def get_styles() -> List[SpeechStyle]:
    """Возвращает список всех стилей."""
    styles = load_styles()
    return [SpeechStyle(name=name, description=desc) for name, desc in styles.items()]


@router.put("")
async def update_styles(style: SpeechStyle):
    """Обновляет существующий стиль выступления."""
    styles = load_styles()
    if style.name not in styles:
        raise HTTPException(status_code=404, detail=f"Стиль с именем '{style.name}' не найден")
    styles[style.name] = style.description
    save_styles(styles)
    return {"message": "Стиль обновлен", "style": style.dict()}
