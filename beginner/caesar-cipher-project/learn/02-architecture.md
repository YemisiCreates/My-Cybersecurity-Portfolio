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
