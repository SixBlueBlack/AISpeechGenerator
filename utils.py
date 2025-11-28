import json
from typing import Dict

STYLES_FILE = "speech_styles.json"


def load_styles() -> Dict[str, str]:
    """Загружает стили выступлений из JSON-файла."""
    try:
        with open(STYLES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_styles(styles: Dict[str, str]):
    """Сохраняет стили выступлений в JSON-файл."""
    with open(STYLES_FILE, 'w') as f:
        json.dump(styles, f, indent=4)
