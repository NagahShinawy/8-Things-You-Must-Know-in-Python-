"""
created by Nagaj at 05/06/2021
"""
PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def contains_punctuation(text: str) -> bool:
    return any(char in PUNCTUATION for char in text)


assert contains_punctuation("How are you ?") is True
assert contains_punctuation("How are you") is False
assert contains_punctuation("you are ok.") is True
assert contains_punctuation("you are ok?") is True

print("ALL PUNCTUATION TESTS HAVE BEEN PASSED")
