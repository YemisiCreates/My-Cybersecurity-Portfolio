# 01 — Cybersecurity Concepts

## Introduction

The Caesar Cipher project demonstrates several foundational concepts in cryptography and cryptanalysis.

Although the Caesar cipher is not secure enough for modern cybersecurity, its simplicity makes it useful for understanding how encryption works, how keys affect ciphertext, and how attackers can analyse weak cryptographic systems.

---

## Plaintext and Ciphertext

**Plaintext** is the original readable information before encryption.

Example:

```text
HELLO WORLD
```

**Ciphertext** is the transformed, unreadable version produced after encryption.

Using a Caesar cipher with a key of `3`:

```text
HELLO WORLD
↓
KHOOR ZRUOG
```

In this example:

```text
Plaintext:  HELLO WORLD
Ciphertext: KHOOR ZRUOG
Key:        3
```

The purpose of encryption is to transform plaintext into ciphertext so that the original information cannot easily be understood without the appropriate key.

---

## Caesar Cipher

The Caesar cipher is a **substitution cipher**.

Each alphabetical character is replaced by another character a fixed number of positions away in the alphabet.

For a key of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

When the end of the alphabet is reached, the shift wraps back to the beginning.

This behaviour is known as **alphabet wrap-around**.

---

## Encryption

Encryption transforms plaintext into ciphertext.

Conceptually:

```text
Plaintext + Key
       ↓
  Encryption
       ↓
  Ciphertext
```

For example:

```text
HELLO WORLD + Key 3
        ↓
   Caesar Cipher
        ↓
KHOOR ZRUOG
```

My tool performs this operation with:

```bash
python3 -m src.main encrypt "HELLO WORLD" --key 3
```

---

## Decryption

Decryption reverses the encryption process.

```text
Ciphertext + Key
        ↓
   Decryption
        ↓
    Plaintext
```

For example:

```text
KHOOR ZRUOG + Key 3
        ↓
   Caesar Cipher
        ↓
HELLO WORLD
```

My tool performs this with:

```bash
python3 -m src.main decrypt "KHOOR ZRUOG" --key 3
```

---

## Cryptographic Keys

A **key** controls the transformation performed by an encryption algorithm.

In a Caesar cipher, the key represents the number of positions each letter is shifted.

For example:

```text
Key 1: A → B
Key 2: A → C
Key 3: A → D
```

Changing the key changes the resulting ciphertext.

However, having a key does not automatically make an encryption system secure. The number of possible keys is also important.

---

## Keyspace

A **keyspace** is the complete set of possible keys that could be used by an encryption algorithm.

The Caesar cipher has only:

```text
26 possible shifts
```

This is an extremely small keyspace.

An attacker can therefore test every possible key instead of trying to guess the correct one.

This is one of the main reasons the Caesar cipher provides almost no security against modern attacks.

---

## Brute-Force Cryptanalysis

A **brute-force attack** systematically tests possible keys until useful plaintext is recovered.

For the Caesar cipher, this means testing all 26 shifts.

My tool can perform this using:

```bash
python3 -m src.main brute-force "KHOOR ZRUOG"
```

The analysis produces candidates such as:

```text
Key  0: KHOOR ZRUOG
Key  1: JGNNQ YQTNF
Key  2: IFMMP XPSME
Key  3: HELLO WORLD
...
```

The correct plaintext exists somewhere within the results because the complete Caesar cipher keyspace has been tested.

This demonstrates an important security principle:

> A cryptographic system with a very small keyspace may be vulnerable even when the attacker does not initially know the key.

---

## Cryptanalysis

**Cryptanalysis** is the study and analysis of cryptographic systems with the aim of understanding or recovering protected information without initially knowing the secret key.

In this project, cryptanalysis involves more than simply decrypting text with a known key.

The tool:

```text
Receives ciphertext
        ↓
Tests possible keys
        ↓
Generates plaintext candidates
        ↓
Analyses those candidates
        ↓
Ranks likely plaintext
        ↓
Suggests a recovered key
```

This turns the project from a basic encryption/decryption program into a small security analysis tool.

---

## Ranked Brute-Force Analysis

A basic brute-force attack gives an analyst all 26 possible results.

However, the analyst would still need to inspect those results manually.

I therefore added **ranked brute-force analysis**.

Instead of only generating candidates, the tool attempts to determine which candidates look most like English.

For example:

```text
Top ranked candidates:

1. Key  3: HELLO WORLD
2. Key  6: EBIIL TLOIA
3. Key 14: WTAAD LDGAS
...
```

The purpose of ranking is not to reduce the keyspace. All possible keys can still be tested.

Instead, ranking helps **prioritise the results that are most likely to be meaningful**.

This is similar to a broader cybersecurity principle: analysts often need to prioritise large amounts of output rather than manually treating every result as equally important.

---

## English-Likelihood Analysis

After brute-force decryption, the tool needs a way to compare candidate plaintexts.

One approach used in this project is **English-likelihood analysis**.

The program examines characteristics of the candidate text that may indicate whether it resembles normal English.

Candidates that appear more consistent with English receive a better ranking than candidates that appear random.

Conceptually:

```text
26 Decryption Candidates
          ↓
   English Analysis
          ↓
      Scoring
          ↓
 Sort by Likelihood
          ↓
Most Likely Plaintext
```

This demonstrates how raw security-tool output can be enriched with analysis to make the results more useful.

---

## Letter-Frequency Analysis

Languages have statistical patterns.

In English, some letters occur much more frequently than others. Letters such as:

```text
E T A O I N
```

generally occur more often than letters such as:

```text
Q X Z J
```

**Frequency analysis** examines these patterns.

My project uses English letter-frequency information as part of the process for evaluating decrypted Caesar cipher candidates.

A candidate whose letter distribution is closer to expected English patterns may receive a stronger score than a candidate containing an unlikely distribution.

Conceptually:

```text
Candidate Plaintext
        ↓
Count Letter Frequencies
        ↓
Compare With Expected
 English Frequencies
        ↓
Generate Analysis Score
```

Frequency analysis is especially relevant to classical substitution ciphers because the underlying statistical characteristics of the language can remain visible after substitution.

---

## File-Based Ciphertext Analysis

Security analysis does not always involve manually entering data directly into a command.

I extended the project so ciphertext can also be read from an evidence file.

For example:

```text
EVIDENCE.TXT
      ↓
Read Ciphertext
      ↓
Brute-Force Analysis
      ↓
Candidate Scoring
      ↓
Candidate Ranking
      ↓
Recovered Key + Plaintext
```

This can be run with:

```bash
python3 -m src.main analyse-file EVIDENCE.TXT
```

For the sample ciphertext:

```text
KHOOR ZRUOG
```

the analysis identifies:

```text
Most likely plaintext: HELLO WORLD
Recovered key: 3
```

This feature helped me think about cryptanalysis as an **analysis workflow**, rather than only as individual encryption and decryption functions.

---

## Why Caesar Cipher Is Insecure

The Caesar cipher should not be used to protect sensitive modern information.

Its major weaknesses include:

- Only 26 possible shifts
- Complete keyspace can be tested quickly
- Language patterns remain present
- Frequency analysis can assist cryptanalysis
- No protection against modern computational attacks

An attacker therefore does not need sophisticated computing resources to break Caesar-encrypted information.

---

## Security Lesson

One of the most important lessons from this project is:

> **Ciphertext is not automatically secure simply because it is unreadable to a human.**

When evaluating encryption, security professionals must consider more than whether the output looks scrambled.

Important considerations include:

```text
Algorithm strength
        +
Keyspace size
        +
Key management
        +
Resistance to cryptanalysis
        +
Implementation security
        ↓
Overall Cryptographic Security
```

Modern cryptography uses algorithms and key sizes designed to make attacks computationally impractical.

The Caesar cipher fails this requirement, but that weakness makes it useful for learning how cryptanalysis works.

---

## Concepts Practised

Through this project I developed practical understanding of:

- Plaintext and ciphertext
- Encryption and decryption
- Substitution ciphers
- Cryptographic keys
- Keyspaces
- Brute-force attacks
- Cryptanalysis
- Candidate ranking
- English-likelihood analysis
- Letter-frequency analysis
- File-based analysis
- Why weak cryptography fails
