"""
created by Nagaj at 05/06/2021
"""
from typing import Tuple

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def contains_punctuation(text: str) -> bool:
    return any(char in PUNCTUATION for char in text)


def is_valid_rgb_2(color: Tuple[int, ...]) -> bool:
    assert len(color) == 3, f"Invalid RGB color values {color}, Must Be (R, G, B)"
    # return all(value in range(0, 256) for value in color)
    return all(0 <= value <= 255 for value in color)


def test_contains_punctuation():
    assert contains_punctuation("python_3") is True
    assert contains_punctuation("How are you?") is True
    assert contains_punctuation("top python web frameworks[django, flask]") is True
    assert contains_punctuation("django2.3") is True


def test_not_contains_punctuation():
    assert contains_punctuation("python") is False
    assert contains_punctuation("testing") is False
    assert contains_punctuation("23") is False
    assert contains_punctuation("") is False


def test_valid_rgb_color():
    assert is_valid_rgb_2((233, 55, 66)) is True
    assert is_valid_rgb_2((233, 255, 255)) is True
    assert is_valid_rgb_2((200, 100, 100)) is True


def test_invalid_rgb_color():
    assert is_valid_rgb_2((233, 55, -66)) is False
    assert is_valid_rgb_2((233, 255, 300)) is False
    assert is_valid_rgb_2((400, 100, 0)) is False
