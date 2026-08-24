from src.analysis import english_score

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")

            shifted = (ord(char) - base + shift) % 26
            result += chr(shifted + base)
        else:
            result += char

    return result

def encrypt(text, key):
    return caesar_cipher(text, key)

def decrypt(text, key):
    return caesar_cipher(text, -key)

def brute_force(text):
    results = []
    for key in range (26):
        decrypted_text = decrypt(text, key)
        results.append((key, decrypted_text))

    return results

def ranked_brute_force(text):
    results = brute_force(text)

    ranked = sorted(
        results,
        key=lambda item: english_score(item[1]),
        reverse=True,
    )

    return ranked
