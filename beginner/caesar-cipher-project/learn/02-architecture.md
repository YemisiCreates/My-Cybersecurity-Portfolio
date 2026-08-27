# 02 — Architecture

## How the Caesar Cipher Tool Is Structured

This project separates the Caesar Cipher functionality into different Python files so that encryption, cryptanalysis, and user interaction are not all handled in one place.

The main components are:

```text
User
  │
  ▼
Command-Line Interface
src/main.py
  │
  ├───────────────┐
  ▼               ▼
Cipher Logic    Analysis Logic
src/cipher.py    src/analysis.py
  │               │
  ▼               ▼
Encrypt         Brute Force
Decrypt         Rank Candidates
                Frequency Analysis
```


### What this section is actually saying

Think of your project like a small security tool with **different departments**.

**`main.py` = the receptionist.**  
It receives what the user types in the Terminal, such as:

```bash
python3 -m src.main ranked-brute-force "KHOOR ZRUOG"

---

## Cryptanalysis Data Flow

When ranked brute-force analysis is performed, the ciphertext moves through the project in several stages.

```text
Ciphertext: "KHOOR ZRUOG"
          │
          ▼
     CLI — main.py
Receives the command and ciphertext
          │
          ▼
     Brute-Force Process
Tests all 26 possible Caesar shifts
          │
          ▼
  26 Plaintext Candidates
          │
          ▼
 Analysis — analysis.py
English-likelihood and
letter-frequency scoring
          │
          ▼
    Candidate Ranking
Most likely results are prioritised
          │
          ▼
       Final Output
Most likely plaintext: HELLO WORLD
Recovered key: 3
```

### 1. Input

The user provides ciphertext through the command line:

```bash
python3 -m src.main ranked-brute-force "KHOOR ZRUOG"
```

`main.py` receives the command and determines that ranked brute-force analysis should be performed.

### 2. Key Testing

The tool tests the complete Caesar Cipher keyspace of 26 possible shifts.

Each key produces a possible plaintext candidate.

### 3. Candidate Analysis

The generated plaintext candidates are analysed using English-likelihood and letter-frequency scoring.

This helps distinguish text that resembles English from less likely results.

### 4. Ranking

The candidates are ranked according to their analysis scores so that the most promising results appear first.

### 5. Analyst Output

The tool presents the highest-ranked candidates and reports the most likely plaintext and recovered key.

For the example ciphertext:

```text
Ciphertext: KHOOR ZRUOG

Most likely plaintext: HELLO WORLD
Recovered key: 3
```

This architecture separates **cipher operations** from **analysis and presentation**, making the cryptanalysis workflow easier to understand and maintain.

---

## File-Based Analysis Flow

The `analyse-file` command extends the same cryptanalysis pipeline by allowing ciphertext to be loaded from a file instead of entered directly into the command line.

```text
EVIDENCE.TXT
     │
     ▼
Read File Contents
     │
     ▼
Extract Ciphertext
"KHOOR ZRUOG"
     │
     ▼
Brute Force All 26 Keys
     │
     ▼
Analyse & Rank Candidates
     │
     ▼
Most Likely Plaintext
"HELLO WORLD"
     │
     ▼
Recovered Key: 3
```

The command is:

```bash
python3 -m src.main analyse-file EVIDENCE.TXT
```

`main.py` opens the specified file and reads the ciphertext. The ciphertext is then passed through the same ranked cryptanalysis process used for command-line input.

This demonstrates how the analysis logic can be reused with different input sources rather than creating a separate cryptanalysis process for each input method.

---

## Architecture Summary

Each component has a specific responsibility:

| Component | Responsibility |
| --- | --- |
| `main.py` | Handles CLI commands, user input, file input and output |
| `cipher.py` | Performs Caesar Cipher encryption, decryption and key testing |
| `analysis.py` | Analyses and scores plaintext candidates |
| `test_cipher.py` | Tests cipher and analysis behaviour |
| `EVIDENCE.TXT` | Provides sample ciphertext for file-based analysis |

Separating these responsibilities makes the project easier to test, debug, maintain and extend.
