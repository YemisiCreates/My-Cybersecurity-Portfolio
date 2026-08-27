# 00 — Overview

## About This Project

The Caesar Cipher Security Analysis Tool is a Python cybersecurity learning project that explores how classical encryption works and how weak encryption can be analysed and broken.

The project started with implementing basic Caesar cipher encryption and decryption. I then extended it from an encryption program into a small cryptanalysis tool capable of brute-forcing all possible Caesar cipher keys, ranking plaintext candidates, performing letter-frequency analysis, and analysing ciphertext stored in an evidence file.

---

## Learning Objectives

By building this project, I aimed to understand:

- How plaintext is transformed into ciphertext
- How encryption and decryption keys work
- How substitution ciphers operate
- Why keyspace size affects cryptographic security
- How brute-force attacks test possible keys
- How cryptanalysis can help identify plaintext
- How English-likelihood scoring can rank decrypted candidates
- How letter-frequency analysis can support cryptanalysis
- How ciphertext can be analysed from an evidence file
- How automated testing can validate security-tool functionality

---

## What the Tool Can Do

The tool supports five main operations:

| Command | Purpose |
| --- | --- |
| `encrypt` | Encrypt plaintext using a Caesar cipher key |
| `decrypt` | Decrypt ciphertext using a known key |
| `brute-force` | Test all 26 possible Caesar cipher shifts |
| `ranked-brute-force` | Rank decrypted candidates to identify likely plaintext |
| `analyse-file` | Read ciphertext from a file and perform ranked cryptanalysis |

---

## Example

Given the ciphertext:

```text
KHOOR ZRUOG
```

The tool can test all 26 possible Caesar cipher keys and determine that the most likely result is:

```text
Recovered key: 3
Most likely plaintext: HELLO WORLD
```

This demonstrates one of the major weaknesses of the Caesar cipher: its keyspace is small enough to exhaust completely.

---

## Prerequisites

To follow this project, it is useful to have a basic understanding of:

- Python fundamentals
- Variables and functions
- Loops and conditionals
- Strings
- Command-line interfaces
- Basic cybersecurity terminology

The project uses:

- Python
- `argparse`
- `pytest`
- Git and GitHub
- A Python virtual environment
- Terminal

---

## Project Components

```text
User Input / EVIDENCE.TXT
          ↓
     CLI (main.py)
          ↓
   Caesar Cipher Engine
      (cipher.py)
          ↓
  Test All 26 Shift Keys
          ↓
26 Plaintext Candidates
          ↓
 English-Likelihood +
Letter-Frequency Analysis
      (analysis.py)
          ↓
    Candidate Ranking
          ↓
 Most Likely Plaintext
    + Recovered Key
```

---

## Learning Modules

This learning section is divided into:

1. **00 — Overview**  
   Project introduction, objectives and prerequisites.

2. **01 — Concepts**  
   Caesar cipher theory, plaintext, ciphertext, keys, keyspace, brute force and frequency analysis.

3. **02 — Architecture**  
   How the components of the tool interact and how ciphertext moves through the analysis pipeline.

4. **03 — Implementation**  
   Walkthrough of the Python implementation and the purpose of the main functions.

5. **04 — Challenges**  
   Limitations, security observations and ideas for extending the project.

---

## Ethical Use

This project was developed for educational and ethical cybersecurity learning.

The cryptanalysis techniques demonstrated here are intended to show why weak encryption mechanisms such as the Caesar cipher are vulnerable to attack.

Testing should only be performed against data, systems and environments that you own or have explicit permission to analyse.
