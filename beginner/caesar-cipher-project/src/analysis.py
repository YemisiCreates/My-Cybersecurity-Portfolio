ENGLISH_LETTER_FREQUENCIES = {
    "a": 8.17,
    "b": 1.49,
    "c": 2.78,
    "d": 4.25,
    "e": 12.70,
    "f": 2.23,
    "g": 2.02,
    "h": 6.09,
    "i": 6.97,
    "j": 0.15,
    "k": 0.77,
    "l": 4.03,
    "m": 2.41,
    "n": 6.75,
    "o": 7.51,
    "p": 1.93,
    "q": 0.10,
    "r": 5.99,
    "s": 6.33,
    "t": 9.06,
    "u": 2.76,
    "v": 0.98,
    "w": 2.36,
    "x": 0.15,
    "y": 1.97,
    "z": 0.07,

}

COMMON_ENGLISH_WORDS = {
    "the",
    "and",
    "is",
    "to",
    "of",
    "in",
    "that",
    "it",
    "hello",
    "world",
    "this",
    "security",
    "cyber",
    "attack",
    "network",
}


COMMON_LETTERS = "etaoinshrdlu"


def english_score(text):
    cleaned_text = text.lower()

    words = cleaned_text.split()

    word_score = sum(
        10 for word in words
        if word.strip(".,!?;:") in COMMON_ENGLISH_WORDS
    )

    letter_score = sum(
        1 for char in cleaned_text
        if char in COMMON_LETTERS
    )

    return word_score + letter_score

def frequency_score(text):
    letters = [char.lower() for char in text if char.isalpha()]

    if not letters:
        return float("inf")

    total_letters = len(letters)
    score = 0.0

    for letter, expected_frequency in ENGLISH_LETTER_FREQUENCIES.items():
        observed_count = letters.count(letter)
        observed_frequency = (observed_count / total_letters) * 100

        score += abs(observed_frequency - expected_frequency)

    return round(score, 2)
