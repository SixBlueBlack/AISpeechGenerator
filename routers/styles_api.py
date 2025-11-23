from fastapi import APIRouter, HTTPException
from typing import List

from schemas.styles import SpeechStyle
from utils import load_styles, save_styles

router = APIRouter()


@router.post("/set_styles")
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


@router.get("/get_styles")
async def get_styles():
    raise HTTPException(status_code=501)


@router.put("/update_styles")
async def update_styles(style: SpeechStyle):
    raise HTTPException(status_code=501)
