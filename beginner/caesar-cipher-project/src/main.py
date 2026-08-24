import argparse

from src.cipher import encrypt, decrypt, brute_force, ranked_brute_force


def main():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher Security Analysis Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Encrypt
    encrypt_parser = subparsers.add_parser(
        "encrypt",
        help="Encrypt plaintext using a Caesar cipher"
    )
    encrypt_parser.add_argument("text", help="Text to encrypt")
    encrypt_parser.add_argument(
        "--key",
        type=int,
        required=True,
        help="Shift key"
    )

    # Decrypt
    decrypt_parser = subparsers.add_parser(
        "decrypt",
        help="Decrypt Caesar cipher ciphertext"
    )
    decrypt_parser.add_argument("text", help="Text to decrypt")
    decrypt_parser.add_argument(
        "--key",
        type=int,
        required=True,
        help="Shift key"
    )

    # Brute force
    brute_parser = subparsers.add_parser(
        "brute-force",
        help="Try all 26 possible Caesar cipher keys"
    )
    brute_parser.add_argument("text", help="Ciphertext to analyse")

    ranked_parser = subparsers.add_parser(
    "ranked-brute-force",
    help="Rank Caesar cipher candidates by English likelihood"
    )

    ranked_parser.add_argument(
    "text",
    help="Ciphertext to analyse"
    )

    file_parser = subparsers.add_parser(
    "analyse-file",
    help="Analyse Caesar cipher ciphertext from a file"
    )

    file_parser.add_argument(
    "file",
    help="Path to ciphertext file"
    )
    args = parser.parse_args()

    if args.command == "encrypt":
        print(encrypt(args.text, args.key))

    elif args.command == "decrypt":
        print(decrypt(args.text, args.key))

    elif args.command == "brute-force":
        results = brute_force(args.text)

        for key, plaintext in results:
            print(f"Key {key:2}: {plaintext}")

    elif args.command == "ranked-brute-force":
        results = ranked_brute_force(args.text)

        best_key, best_plaintext = results[0]

        print("\n=== Caesar Cipher Cryptanalysis ===")
        print(f"Ciphertext: {args.text}")
        print("Keys analysed: 26")
        print("\nTop 5 ranked candidates:")
        print("-" * 50)

        for rank, (key, plaintext) in enumerate(results[:5], start=1):
            print(f"{rank}. Key {key:2}: {plaintext}")

        print("-" * 50)
        print(f"Most likely plaintext: {best_plaintext}")
        print(f"Recovered key: {best_key}")

    elif args.command == "analyse-file":
        with open(args.file, "r") as file:
            ciphertext = file.read().strip()

        results = ranked_brute_force(ciphertext)
        best_key, best_plaintext = results[0]

        print("\n=== Caesar Cipher File Analysis ===")
        print(f"File: {args.file}")
        print(f"Ciphertext: {ciphertext}")
        print("Keys analysed: 26")
        print("\nTop 5 ranked candidates:")
        print("-" * 50)

        for rank, (key, plaintext) in enumerate(results[:5], start=1):
            print(f"{rank}. Key {key:2}: {plaintext}")

        print("-" * 50)
        print(f"Most likely plaintext: {best_plaintext}")
        print(f"Recovered key: {best_key}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
