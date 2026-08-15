# 02 — Architecture

## System Overview

The Base64 Security Analysis Tool uses a modular architecture. Each Python module has a specific responsibility, while the modules work together as one analysis pipeline.

At a high level:

              User Input  
                  ↓  
                 CLI  
                  ↓  
           Input Processing  
                  ↓  
    Detection / Encoding / Decoding  
                  ↓  
       Recursive Layer Analysis  
                  ↓  
              Formatting  
                  ↓  
           Terminal Output

The main package contains:

- `cli.py`
- `constants.py`
- `detector.py`
- `encoders.py`
- `formatter.py`
- `peeler.py`
- `utils.py`

 ### Project Module Structure

![Base64 Tool Module Architecture](../assets/architecture-files.png)

*Figure 1: Python modules that make up the Base64 Security Analysis Tool.*

---

## 1. `cli.py` — Command-Line Interface

`cli.py` is the main entry point between the user and the application.

It receives commands such as:

- `encode`
- `decode`
- `detect`
- `chain`
- `peel`

The CLI interprets the user's request and routes the data to the appropriate module.

For example:

`b64tool detect DATA`

follows approximately:

User  
→ `cli.py`  
→ `detector.py`  
→ `formatter.py`  
→ Terminal Output

For:

`b64tool peel DATA`

the CLI sends the input to the recursive peeling logic instead.

The CLI therefore acts as the controller of the application rather than performing every operation itself.

---

## 2. `utils.py` — Input & Helper Functions

`utils.py` contains reusable helper functions.

Functions inspected include:

- `resolve_input_bytes()` — retrieves input as bytes
- `resolve_input_text()` — retrieves input as text
- `truncate()` — limits the length of displayed data
- `safe_bytes_preview()` — creates a safe preview of decoded bytes
- `is_printable_text()` — checks whether decoded data is mostly human-readable

Input can come directly from the command line, from a file, or through standard input.

These helpers prevent common logic from being repeated throughout the application.

---

## 3. `constants.py` — Rules & Configuration

`constants.py` contains the fixed values used by the tool.

Examples include:

`CONFIDENCE_THRESHOLD = 0.6`

This means a detection normally needs at least 60% confidence to be considered valid.

The module also contains:

- Detection scoring weights
- Supported character sets
- Minimum input length
- Preview length
- Printable-text threshold
- Maximum recursive peeling depth

For example:

`PEEL_MAX_DEPTH = 20`

provides an upper limit on recursive decoding.

The scoring weights are used by the detector to calculate confidence based on multiple characteristics of the input.

---

## 4. `detector.py` — Confidence-Based Format Detection

`detector.py` attempts to determine which encoding format best matches unknown input.

It does not rely on a single pattern.

Instead, each supported format has scoring logic that examines multiple characteristics.

For Hex, this can include:

- Valid hexadecimal characters
- Even input length
- Presence of `A-F`
- Consistent casing
- Successful decoding
- Whether the decoded result is printable

Different evidence contributes to the overall confidence score.

For example:

Hex → 80% — detected  
Base64 → 50% — below threshold

### Detection in Practice

![Encoding Detection Confidence Scores](../assets/Detection-score.png)

*Figure 2: Verbose detection output showing Hex identified at 80% confidence while Base64 scored 50% and remained below the configured 60% threshold.*

This demonstrates how the detector evaluates multiple possible formats instead of assuming the input belongs to a single encoding type.

Because the confidence threshold is 60%, Hex is accepted while the weaker Base64 match is not.

This creates evidence-based detection rather than simple yes/no pattern matching.

---

## 5. `encoders.py` — Encoding & Decoding Engine

`encoders.py` performs the actual data transformations.

The tool supports:

- Base64
- Base64URL
- Base32
- Hex
- URL encoding

The module contains an encoder registry that maps each supported format to the correct encoding and decoding functions.

Conceptually:

Detected format  
↓  
Select matching decoder  
↓  
Decode data  
↓  
Return decoded bytes

For example, if `detector.py` identifies Hex with high confidence, `encoders.py` selects the Hex decoder and converts the encoded string back into its underlying data.

The module also contains safe decoding behaviour so failed decoding attempts can return `None` instead of being treated as successful results.

---

## 6. `peeler.py` — Recursive Layer Analysis

`peeler.py` coordinates recursive decoding.

Its workflow is:

Input  
↓  
Detect strongest format  
↓  
Check confidence threshold  
↓  
Decode layer  
↓  
Analyse decoded result again  
↓  
Repeat or stop

The peeler stops when:

- No encoding is detected
- Confidence is below the threshold
- Decoding fails
- Maximum depth is reached

During testing, I demonstrated:

Hex — 80%  
↓  
Base64 — 95%  
↓  
`Security Analysis Demo`

This shows how multiple encoding layers can be automatically removed.

The `--max-depth` option provides additional control over how many layers are processed.

---

## 7. `formatter.py` — Analyst-Friendly Output

`formatter.py` controls how results are presented in the terminal.

It produces output including:

- Detection tables
- Confidence percentages
- Layer information
- Verbose score breakdowns
- Encoding-chain results
- Final decoded output

For example, `detector.py` may calculate:

`Hex = 80%`

while `formatter.py` turns that result into a readable coloured table for the analyst.

This keeps the analysis logic separate from the presentation logic.

---

## 8. Detection Workflow

A normal detection request follows:

User Input  
↓  
`cli.py`  
↓  
`utils.py` prepares input  
↓  
`detector.py` scores supported formats  
↓  
`constants.py` provides scoring rules and threshold  
↓  
Best valid candidate selected  
↓  
`formatter.py` displays results

---

## 9. Recursive Peeling Workflow

A recursive analysis follows:

Unknown Input  
↓  
`cli.py`  
↓  
`peeler.py`  
↓  
`detector.py`  
↓  
Confidence high enough?  
↓ Yes  
`encoders.py` decodes layer  
↓  
Decoded result returned to detector  
↓  
Another valid layer?  
↓ Yes → Repeat  
↓ No  
`formatter.py`  
↓  
Final Output

Example:

`Hex → Base64 → Security Analysis Demo`

---

## 10. Chain vs Peel

The tool supports two different multi-layer workflows.

### Chain

`chain` applies encoding methods chosen by the user.

Example:

Plaintext  
→ Base64  
→ Hex

### Peel

`peel` analyses unknown data and attempts to discover and remove the layers automatically.

Example:

Unknown Data  
→ Detect Hex  
→ Decode  
→ Detect Base64  
→ Decode  
→ Plaintext

`chain` creates layers.

`peel` investigates and removes them.

---

## 11. Why This Architecture Works

Separating the project into modules makes the tool easier to:

- Understand
- Debug
- Test
- Maintain
- Extend
- Reuse

Each module has a clear responsibility.

`cli.py` — receives commands  
`utils.py` — handles common helper tasks  
`constants.py` — provides rules and thresholds  
`detector.py` — identifies likely encodings  
`encoders.py` — performs transformations  
`peeler.py` — coordinates recursive analysis  
`formatter.py` — presents results

> **Key takeaway:** The tool separates detection, transformation, recursion, configuration, input handling and presentation while connecting them through a single analysis workflow.
