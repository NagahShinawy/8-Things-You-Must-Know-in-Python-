"""
created by Nagaj at 05/06/2021
"""


def has_digit(text: str) -> bool:
    for char in text:
        if char.isdigit():
            return True
    return False


def has_digit_2(text: str) -> bool:
    return any(char.isdigit() for char in text)


assert has_digit("john") is False
assert has_digit("john2") is True
assert has_digit("te23st") is True
assert has_digit("test") is False

print("ALL TEST HAVE BEEN PASSED")

print("#" * 50)

assert has_digit_2("python") is False
assert has_digit_2("python3") is True
assert has_digit_2("django3") is True
assert has_digit_2("django") is False

print("ALL TEST HAVE BEEN PASSED")
