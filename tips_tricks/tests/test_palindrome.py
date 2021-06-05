"""
created by Nagaj at 05/06/2021
"""

import re


def remove_punctuation(words):
    """Helper function to return a string, removing all punctuations and spaces"""
    return re.sub(r"\W+", "", words)


def is_palindrome(text: str):
    txt = remove_punctuation(text.lower())
    return txt == txt[::-1]


def is_palindrome2(text: str):
    txt = remove_punctuation(text.lower())
    return txt == "".join([char for char in reversed(txt)])  # not recommended


def test_palindrome():
    assert is_palindrome("radar") is True
    assert is_palindrome("Radar") is True
    assert is_palindrome("bob") is True
    assert is_palindrome("level") is True
    assert is_palindrome("refer") is True
    assert is_palindrome("php") is True


def test_not_palindrome():
    assert is_palindrome("python") is False
    assert is_palindrome("java") is False
    assert is_palindrome("django") is False


def test_is_palindrome():
    print("\n", is_palindrome2("php"))
