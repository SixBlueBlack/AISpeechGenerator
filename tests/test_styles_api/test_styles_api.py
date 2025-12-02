import json
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

TEST_STYLES_FILE = Path(__file__).parent / "speech_styles.json"


def load_styles() -> dict:
    if not TEST_STYLES_FILE.exists():
        return {}
    try:
        with open(TEST_STYLES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_styles(styles: dict):
    with open(TEST_STYLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(styles, f, indent=4, ensure_ascii=False)


# Подмена ДО импорта app
# Просто делаем это в глобальной области
import utils
utils.load_styles = load_styles
utils.save_styles = save_styles


# === Удаляем тестовый файл ===
if TEST_STYLES_FILE.exists():
    TEST_STYLES_FILE.unlink()


# === Теперь импортируем app ===
from main import app
client = TestClient(app)


# === Тесты===
class TestStylesAPI:

    def test_initial_get_returns_empty(self):
        response = client.get("/api/styles")
        assert response.status_code == 200
        assert response.json() == {"styles": {}}

    def test_post_new_styles_success(self):
        payload = [
            {"name": "professional", "description": "Официальный деловой стиль"},
            {"name": "motivational", "description": "Вдохновляющий и энергичный"},
            {"name": "friendly", "description": "Дружелюбный, неформальный"},
        ]
        response = client.post("/api/styles", json=payload)
        assert response.status_code == 200

    def test_get_after_post_returns_correct_data(self):
        response = client.get("/api/styles")
        assert response.status_code == 200
        styles = response.json()["styles"]
        assert styles["professional"] == "Официальный деловой стиль"
        assert styles["motivational"] == "Вдохновляющий и энергичный"
        assert styles["friendly"] == "Дружелюбный, неформальный"

    def test_post_duplicate_style_fails(self):
        response = client.post("/api/styles", json=[{"name": "professional", "description": "дубликат"}])
        assert response.status_code == 400

    def test_put_updates_existing_style(self):
        response = client.put("/api/styles", json={"name": "motivational", "description": "МОТИВАЦИЯ!!!"})
        assert response.status_code == 200

    def test_put_nonexistent_style_returns_404(self):
        response = client.put("/api/styles", json={"name": "ghost", "description": "404"})
        assert response.status_code == 404

    def test_get_after_update_has_new_description(self):
        response = client.get("/api/styles")
        assert response.status_code == 200
        assert response.json()["styles"]["motivational"] == "МОТИВАЦИЯ!!!"

    def test_post_invalid_payload_missing_name(self):
        response = client.post("/api/styles", json=[{"description": "без имени"}])
        assert response.status_code == 422

    def test_put_invalid_payload_missing_name(self):
        response = client.put("/api/styles", json={"description": "только описание"})
        assert response.status_code == 422
