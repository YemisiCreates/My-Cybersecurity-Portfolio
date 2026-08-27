# 03 — Implementation

## Implementation Overview

The Caesar Cipher Security Analysis Tool is written in Python and separates the core cipher operations, cryptanalysis logic, command-line interface, and testing into different components.

The main implementation files are:

```text
src/
├── cipher.py
├── analysis.py
└── main.py

tests/
└── test_cipher.py
```

Each file has a specific responsibility:

- **`cipher.py`** contains the core Caesar Cipher operations.
- **`analysis.py`** contains the logic used to analyse and score plaintext candidates.
- **`main.py`** provides the command-line interface and connects the different components.
- **`test_cipher.py`** contains automated tests used to verify expected behaviour.

---

## Caesar Cipher Logic

The core cipher logic works by shifting alphabetical characters according to a numerical key.

For example, with a key of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

The implementation must also account for **alphabet wrap-around**. When a shift moves beyond `Z`, it returns to the beginning of the alphabet.

Conceptually:

```text
Letter
  ↓
Determine Alphabet Position
  ↓
Apply Shift Key
  ↓
Wrap Within 26 Letters
  ↓
Convert Back to Character
```

Non-alphabetic characters such as spaces and punctuation are preserved rather than shifted.

This allows input such as:

```text
HELLO, WORLD!
```

to retain its formatting while the alphabetical characters are transformed.

---

## Encryption

Encryption applies the selected shift to the plaintext.

The user can run:

```bash
python3 -m src.main encrypt "HELLO WORLD" --key 3
```

The program returns:

```text
KHOOR ZRUOG
```

Conceptually:

```text
Plaintext + Key
      ↓
Caesar Shift
      ↓
Ciphertext
```

---

## Decryption

Decryption reverses the shift used during encryption.

For example:

```bash
python3 -m src.main decrypt "KHOOR ZRUOG" --key 3
```

returns:

```text
HELLO WORLD
```

Rather than treating decryption as an unrelated process, the implementation reverses the transformation performed during encryption.

This demonstrates how encryption and decryption operations are mathematically related.

---

## Brute-Force Implementation

Because the Caesar Cipher has only 26 possible shifts, the tool can test the entire keyspace.

The brute-force process follows this logic:

```text
Ciphertext
    ↓
Start with Key 0
    ↓
Decrypt Candidate
    ↓
Store Result
    ↓
Try Next Key
    ↓
Repeat Until All 26 Keys Are Tested
```

For example:

```bash
python3 -m src.main brute-force "KHOOR ZRUOG"
```

produces candidates including:

```text
Key  0: KHOOR ZRUOG
Key  1: JGNNQ YQTNF
Key  2: IFMMP XPSME
Key  3: HELLO WORLD
...
```

This implementation demonstrates **exhaustive key search**: rather than attempting to guess the encryption key, every possible key in the Caesar Cipher keyspace is evaluated.

---

## Ranked Cryptanalysis

Brute force successfully generates all possible plaintexts, but it does not automatically determine which result is correct.

To improve this, I implemented a ranking stage.

```text
Ciphertext
    ↓
Generate 26 Candidates
    ↓
Analyse Each Candidate
    ↓
Calculate Likelihood Scores
    ↓
Sort Candidates by Score
    ↓
Return Highest-Ranked Results
```

This allows the tool to produce output such as:

```text
Top 5 ranked candidates:

1. Key  3: HELLO WORLD
2. Key  6: EBIIL TLOIA
3. Key 14: WTAAD LDGAS
```

The highest-ranked candidate is then reported as the most likely plaintext together with its recovered key.

---

## English-Likelihood and Frequency Analysis

The analysis component helps distinguish meaningful plaintext from unlikely character combinations.

Rather than treating every brute-force result equally, candidate plaintexts are assigned scores based on characteristics associated with English text.

Letter-frequency analysis also considers how closely the distribution of letters resembles expected English-language patterns.

Common English letters include:

```text
E T A O I N
```

while letters such as:

```text
Q X Z J
```

generally occur less frequently.

The analysis process can therefore be represented as:

```text
Plaintext Candidate
       ↓
English-Likelihood Analysis
       +
Letter-Frequency Analysis
       ↓
Candidate Score
       ↓
Ranking
```

This does not make Caesar Cipher cryptanalysis computationally difficult—the entire keyspace is still only 26 shifts. Instead, the scoring logic helps automate the **prioritisation and interpretation of brute-force results**.

---

## Command-Line Interface Implementation

The project uses Python's `argparse` module to provide a command-line interface.

The CLI allows the user to select different operations without changing the Python source code.

The available commands are:

```text
encrypt
decrypt
brute-force
ranked-brute-force
analyse-file
```

Conceptually, `main.py` acts as the controller:

```text
User Command
     ↓
   argparse
     ↓
Identify Requested Operation
     ↓
Call Appropriate Function
     ↓
Display Result
```

For example:

```bash
python3 -m src.main encrypt "HELLO WORLD" --key 3
```

selects the encryption operation, while:

```bash
python3 -m src.main ranked-brute-force "KHOOR ZRUOG"
```

selects the ranked cryptanalysis workflow.

Using subcommands keeps the interface organised while allowing multiple security-analysis operations to be accessed through one tool.

---

## File-Based Analysis Implementation

The `analyse-file` command allows ciphertext to be loaded from a file rather than supplied directly as a command-line string.

Example:

```bash
python3 -m src.main analyse-file EVIDENCE.TXT
```

The implementation follows this process:

```text
File Path
   ↓
Open File
   ↓
Read Ciphertext
   ↓
Remove Unnecessary Surrounding Whitespace
   ↓
Pass Ciphertext to Ranked Cryptanalysis
   ↓
Analyse 26 Candidates
   ↓
Display Most Likely Plaintext + Key
```

The file is read in `main.py`, after which the existing ranked brute-force functionality is reused.

This is important from a software-design perspective because the cryptanalysis logic does not need to be rewritten simply because the input comes from a file.

---

## Output Presentation

The ranked analysis output is designed to give the user useful information without requiring them to inspect all 26 candidates manually.

The output includes:

```text
Ciphertext
Number of keys analysed
Top-ranked candidates
Most likely plaintext
Recovered key
```

For example:

```text
=== Caesar Cipher Cryptanalysis ===
Ciphertext: KHOOR ZRUOG
Keys analysed: 26

Top 5 ranked candidates:
...

Most likely plaintext: HELLO WORLD
Recovered key: 3
```

This separates **analysis** from **presentation**: the underlying functions generate and rank the results, while the CLI presents those findings in a format that is easier for a user or analyst to interpret.---

## Automated Testing

I used `pytest` to verify that the cipher and cryptanalysis functionality behaves as expected.

Automated testing was important because changes to the analysis functionality could unintentionally affect existing encryption, decryption, or brute-force behaviour.

The test suite currently contains **11 passing tests**.

It validates areas including:

- Encryption with a known key
- Decryption with a known key
- Lowercase character handling
- Preservation of spaces and punctuation
- Alphabet wrap-around
- Brute-force recovery of plaintext
- Coverage of all 26 Caesar Cipher keys
- Ranked brute-force identification of likely plaintext
- Ranked brute-force coverage of the complete keyspace
- English-likelihood scoring
- Letter-frequency analysis

The tests can be run with:

```bash
python3 -m pytest tests/test_cipher.py -v
```

A successful test run confirms:

```text
11 passed
```

### Why Testing Matters

Testing helps ensure that adding new functionality does not silently break existing behaviour.

For example, when ranked cryptanalysis and frequency analysis were added, the existing encryption and decryption operations still needed to produce the same expected results.

The testing workflow therefore became:

```text
Implement Feature
      ↓
Run Test Suite
      ↓
Verify Expected Behaviour
      ↓
Debug Failures
      ↓
Run Tests Again
      ↓
All Tests Pass
```

This introduced me to the idea of **regression testing**: previously working functionality should continue to work after the codebase is changed.

---

## Implementation Summary

The completed implementation combines several layers:

```text
CLI Input / Evidence File
          ↓
     Input Handling
          ↓
 Caesar Cipher Operations
          ↓
   Exhaustive Key Search
          ↓
   Candidate Generation
          ↓
English-Likelihood +
Frequency Analysis
          ↓
   Candidate Ranking
          ↓
 Analyst-Friendly Output
          ↓
    Automated Testing
```

Building the project in stages helped me move from implementing a simple cipher to creating a small cryptanalysis tool with automated analysis, file-based input, structured CLI commands, and test coverage.
