# 04 — Challenges, Limitations & Future Improvements

## Development Challenges

Building the Caesar Cipher Security Analysis Tool involved several challenges as the project developed from a basic cipher into a small cryptanalysis tool.

Working through these problems helped me improve my understanding of Python, debugging, testing, cryptanalysis, and software structure.

---

## Challenge 1 — Python Indentation and Control Flow

One recurring challenge was maintaining correct indentation while extending the command-line interface.

The CLI uses an `if / elif / else` structure to determine which operation the user requested:

```text
encrypt
   ↓
decrypt
   ↓
brute-force
   ↓
ranked-brute-force
   ↓
analyse-file
```

When new commands were introduced, incorrect indentation caused errors such as:

```text
SyntaxError
IndentationError
```

For example, an `elif` placed at the wrong indentation level was no longer recognised as part of the original conditional chain.

### What I Learned

Python indentation is part of the program's syntax, not simply formatting.

I learned to inspect the surrounding code instead of assuming that the line mentioned in an error message was necessarily the original cause.

I also used syntax checking:

```bash
python3 -m py_compile src/main.py
```

before running the complete program.

This provided a quicker way to confirm that syntax and indentation were valid.

---

## Challenge 2 — Moving Beyond Basic Brute Force

The first brute-force implementation successfully tested all 26 Caesar Cipher keys.

However, this produced 26 possible plaintext results and still required a person to determine which result was meaningful.

The challenge therefore became:

> How can the tool help prioritise the most likely plaintext instead of only displaying every possible result?

I extended the project with ranked brute-force analysis.

The process became:

```text
Ciphertext
    ↓
Test 26 Keys
    ↓
Generate 26 Candidates
    ↓
Analyse Candidates
    ↓
Assign Scores
    ↓
Rank Results
    ↓
Suggest Most Likely Plaintext
```

### What I Learned

Generating security data and **analysing** security data are different problems.

A tool can produce technically correct results while still requiring additional analysis to make those results useful.

Adding candidate ranking helped transform the project from a basic cipher program into a more analytical cybersecurity project.

---

## Challenge 3 — Improving Plaintext Analysis

Ranking candidate plaintext required a method for deciding which results were more likely to contain meaningful English.

I explored English-likelihood scoring and letter-frequency analysis to improve this process.

The analysis considers patterns associated with English text and uses them to score the decrypted candidates.

### Limitation

Frequency analysis is not guaranteed to identify the correct plaintext in every situation.

Very short messages may not contain enough letters to produce a representative frequency distribution, and unusual words or non-English text may also receive misleading scores.

This means the highest-ranked result should be treated as the **most likely candidate**, rather than unquestionable proof that the plaintext is correct.

### What I Learned

Automated analysis can help prioritise findings, but an analyst still needs to understand the limitations of the method being used.

This is an important cybersecurity principle because automated tools can produce false positives, false negatives, or misleading rankings when their assumptions do not match the data being analysed.


---

## Challenge 4 — Adding File-Based Analysis

The original tool accepted ciphertext directly from the command line.

I later extended it so ciphertext could also be loaded from an evidence file:

```bash
python3 -m src.main analyse-file EVIDENCE.TXT
```

This required the CLI to:

```text
Receive File Path
      ↓
Open File
      ↓
Read Ciphertext
      ↓
Pass Ciphertext to Existing Analysis
      ↓
Return Ranked Results
```

An important design decision was to **reuse the existing cryptanalysis functionality** rather than create a completely separate analysis process for files.

### What I Learned

Separating input handling from analysis logic makes functionality easier to reuse.

Whether ciphertext comes directly from the command line or from a file, the same underlying cryptanalysis process can analyse it.

---

## Challenge 5 — Testing While Extending the Project

As new features were added, I needed to make sure that existing functionality continued to work.

The project eventually included tests covering encryption, decryption, brute force, candidate ranking, English-likelihood scoring, and frequency analysis.

The final test suite produced:

```text
11 passed
```

Testing became particularly useful after modifying analysis functionality because a change intended to improve one feature could potentially affect another.

### What I Learned

I developed a simple development cycle:

```text
Make Change
    ↓
Check Syntax
    ↓
Run Feature
    ↓
Run Tests
    ↓
Investigate Failure
    ↓
Correct Code
    ↓
Test Again
```

This helped me understand the value of **regression testing** when extending an existing codebase.

---

## Current Limitations

The project intentionally uses the Caesar Cipher as a learning example, so it has several limitations:

- The Caesar Cipher itself is cryptographically insecure.
- The complete keyspace contains only 26 shifts.
- Frequency analysis becomes less reliable with very short ciphertext.
- English-language scoring assumes the plaintext resembles English.
- The highest-ranked candidate may not always be the correct plaintext.
- The tool currently focuses specifically on Caesar Cipher cryptanalysis.
- File analysis currently demonstrates a simple text-based evidence workflow rather than a full digital-forensics process.

These limitations are important because security tools should not be evaluated only by whether they produce output. Their assumptions and boundaries also need to be understood.

---

## Future Improvements

Possible future extensions include:

### 1. Improved Language Detection

The ranking system could use additional language characteristics, such as common words, n-grams, or more advanced statistical models.

### 2. Support for Additional Classical Ciphers

The project could be extended to analyse other classical cryptographic techniques, such as:

```text
Vigenère Cipher
Affine Cipher
Atbash Cipher
Substitution Ciphers
```

### 3. Multiple Language Profiles

Frequency-analysis profiles could be added for languages other than English.

### 4. Structured Analysis Reports

Instead of displaying results only in the Terminal, analysis findings could be exported to formats such as JSON or CSV for further investigation.

### 5. Improved File Handling

Future versions could validate file paths, handle unreadable or empty files more gracefully, and provide clearer error messages.

---

## Final Reflection

This project began as an implementation of a simple classical cipher but developed into a broader exercise in cybersecurity analysis.

I moved through several stages:

```text
Encryption / Decryption
          ↓
     Brute Force
          ↓
   Candidate Ranking
          ↓
  Frequency Analysis
          ↓
 File-Based Analysis
          ↓
 Automated Testing
          ↓
Documentation & Review
```

The most important lesson was that building a security tool involves more than producing technically correct output.

It also requires understanding the weakness being demonstrated, analysing results, recognising limitations, testing changes, handling errors, and communicating findings clearly.

The Caesar Cipher is not appropriate for modern security, but implementing and analysing it provided a practical foundation for understanding concepts that appear in more advanced cryptography and cybersecurity analysis.





