# Hash Cracker Project

## Project Overview

This project focused on password hash cracking concepts using a multi-threaded C++ hash cracking tool.

The tool is designed to support:
- MD5
- SHA1
- SHA256
- SHA512
- Dictionary attacks
- Brute-force attacks
- Rule-based mutations
- Salted hashes

---

## What I Learned

- Password hashes are one-way representations of passwords.
- Weak passwords can be recovered using dictionary attacks.
- Hash type can often be identified by hash length.
- Rule-based attacks mutate common passwords using patterns such as capitalization, leetspeak, reversed words, and appended digits.
- Multi-threading can improve cracking speed by splitting work across CPU cores.
- Salted hashes make attacks harder by adding extra data before or after the password.

---

## Troubleshooting Notes

During setup, I installed required build dependencies including CMake, Ninja, OpenSSL, and Boost using Homebrew.

The build failed because my current macOS C++ compiler did not fully support required modern C++ features used by the project.

Errors encountered included:

- `fatal error: 'generator' file not found`
- `no member named 'jthread' in namespace 'std'`

This indicates the project requires newer C++20/C++23 compiler support than the default compiler available on my Mac.

---

## Skills Practiced

- Password security fundamentals
- Hashing concepts
- Dictionary attack concepts
- Brute-force attack concepts
- Rule-based mutation concepts
- C++ build troubleshooting
- CMake/Ninja build workflows
- macOS development environment troubleshooting

---

## Interview Talking Points

This project helped me understand password hash cracking at a conceptual level, including dictionary attacks, brute-force attacks, rule-based mutations, salted hashes, and hash algorithm identification.

Although the build failed due to compiler compatibility limitations, I was able to diagnose the issue from the build logs and identify that the project requires newer C++ standard library support
