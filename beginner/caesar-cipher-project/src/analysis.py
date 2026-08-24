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
