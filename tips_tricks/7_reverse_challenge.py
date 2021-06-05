"""
created by Nagaj at 05/06/2021
"""
import re


def remove_punctuation(words):
    """Helper function to return a string, removing all punctuations and spaces"""
    return re.sub(r"\W+", "", words)


def palindrome(text: str):
    text = remove_punctuation(text.lower())
    return text == text[::-1]


print(palindrome("test"))
print(palindrome("python"))
print(palindrome("bob"))
print(palindrome("radar"))
print(palindrome("Radar"))
print(palindrome("Radar ?.!"))
