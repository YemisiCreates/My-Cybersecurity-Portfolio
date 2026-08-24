from src.cipher import encrypt, decrypt, brute_force, ranked_brute_force
from src.analysis import english_score, frequency_score


def test_encrypt_with_key_three():
    result = encrypt("HELLO WORLD", 3)
    assert result == "KHOOR ZRUOG"

def test_decrypt_with_key_three():
    result = decrypt("KHOOR ZRUOG", 3)
    assert result == "HELLO WORLD"

def test_lowercase_encryption():
    result = encrypt("hello", 3)
    assert result == "khoor"


def test_preserves_spaces_and_punctuation():
    result = encrypt("HELLO, WORLD!", 3)
    assert result == "KHOOR, ZRUOG!"


def test_wraps_alphabet():
    result = encrypt("XYZ", 3)
    assert result == "ABC"


def test_brute_force_contains_original_plaintext():
    results = brute_force("KHOOR")
    assert (3, "HELLO") in results


def test_brute_force_tries_all_keys():
    results = brute_force("KHOOR")
    assert len(results) == 26

def test_ranked_brute_force_finds_correct_plaintext():
    results = ranked_brute_force("KHOOR ZRUOG")

    assert any(
        key == 3 and plaintext == "HELLO WORLD"
        for key, plaintext in results
    )


def test_ranked_brute_force_returns_all_keys():
    results = ranked_brute_force("KHOOR ZRUOG")

    assert len(results) == 26

def test_english_score_prefers_english_text():
    english = english_score("HELLO WORLD")
    nonsense = english_score("XQZJK VBNMP")

    assert english > nonsense


def test_frequency_score_returns_number():
    score = frequency_score("HELLO WORLD")

    assert isinstance(score, (int, float))
