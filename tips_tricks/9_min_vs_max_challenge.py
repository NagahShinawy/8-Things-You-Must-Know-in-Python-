"""
created by Nagaj at 05/06/2021
"""
DICTIONARY = "dictionary.txt"

letter_scores = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def get_scrabble_dictionary():
    with open(DICTIONARY, "r", encoding="utf-8") as file:
        content = file.read().splitlines()
    return content


def score_word(word: str):
    """Return the score for a word using letter_scores.
        If the word isn't in DICTIONARY, it gets a score of 0."""
    words = get_scrabble_dictionary()
    if word.upper() in words:
        return sum(letter_scores.get(char, 0) for char in word)
    return 0


def get_word_largest_score(sentence: str):
    """Given a sentence, return the word with the largest score."""
    # word = max([word for word in sentence.split()], key=score_word)
    # return max([word for word in sentence.split()], key=score_word)
    max_word_by_score = max([word for word in sentence.split()], key=score_word)
    return {
        max_word_by_score: score_word(max_word_by_score)
    }


print(get_word_largest_score("what do you think"))
