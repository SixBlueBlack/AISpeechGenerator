import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from schemas.model import ModelSettings


from ai.model_parameters import (
    do_sample,
    max_length,
    max_new_tokens,
    temperature,
    top_p,
    top_k,
    repetition_penalty
)


@pytest.fixture
def model_parameters():
    """Фикстура возвращает все параметры модели по умолчанию"""
    return ModelSettings(
        do_sample=do_sample,
        max_length=max_length,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty
    )


@pytest.fixture
def sample_model_parameters():
    """Фикстура возвращает тестовые параметры модели"""
    return ModelSettings(
        do_sample=False,
        max_length=1024,
        max_new_tokens=512,
        temperature=0.5,
        top_p=0.8,
        top_k=30,
        repetition_penalty=1.2
    )


@pytest.fixture
def model_parameters_module():
    """Фикстура возвращает сам модуль с параметрами"""
    from ai import model_parameters
    return model_parameters