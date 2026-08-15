# Concepts

## 1. Encoding Is Not Encryption

Encoding and encryption both transform data, but they have different purposes.

**Encoding** changes data into another format so that it can be stored, transmitted, or interpreted by different systems. It does not require a secret key and is designed to be reversible.

Examples include:
- Base64
- Base32
- Hexadecimal
- URL encoding

**Encryption**, however, is a security mechanism. It transforms readable data (plaintext) into unreadable data (ciphertext) using a cryptographic algorithm and a key. The correct key is required to recover the original data.

Examples include:
- AES
- RSA
- ChaCha20

### Why This Matters in Cybersecurity

Encoded data should never automatically be considered secure simply because it is unreadable to a human.

For example:

`Hello Yemisi`

can be Base64 encoded as:

`SGVsbG8gWWVtaXNp`

The result looks obscure, but anyone who recognises Base64 can decode it without a password or secret key.

For a security analyst, recognising this difference is important when analysing suspicious payloads, logs, network traffic, scripts, and other potentially obfuscated data.

> **Key takeaway:** Encoding changes how data is represented. Encryption is designed to protect the confidentiality of data.

## 2. Why Encoding Matters in Cybersecurity

Encoding appears frequently in cybersecurity because data is not always presented in a directly readable form.

Security analysts may encounter encoded data in:

- Network traffic and packet captures
- HTTP requests and URLs
- Application and system logs
- API requests and tokens
- Scripts and command-line activity
- Suspicious files and malware

### Encoding Can Be Used for Obfuscation

Encoding is not inherently malicious. However, attackers can use it to make suspicious content harder to recognise.

For example, instead of displaying:

`Security Analysis Demo`

an encoded value may appear as:

`U2VjdXJpdHkgQW5hbHlzaXMgRGVtbw==`

The information has not been encrypted. It has simply been represented differently.

An analyst who recognises the encoding can decode the value and continue investigating its contents.

### Multiple Encoding Layers

Data can also be encoded more than once.

For example:

`Original text → Base64 → Hex`

This creates multiple layers that must be decoded in reverse order:

`Hex → Base64 → Original text`

This is particularly important to this project because the CLI can detect and peel multiple encoding layers automatically.

> **Security analyst mindset:** When a suspicious value looks unreadable, do not immediately assume it is encrypted. First investigate whether it may be encoded or obfuscated.

## 3. Base64 Encoding

Base64 is an encoding method that converts binary data into a text-based format using 64 printable characters.

The Base64 character set contains:

- Uppercase letters: `A-Z`
- Lowercase letters: `a-z`
- Numbers: `0-9`
- Two additional characters: `+` and `/`
- The `=` character may be used for padding

### How Base64 Works

Computers represent data using bits. Base64 takes the binary representation of data and processes it in groups of **6 bits**.

Why 6 bits?

A group of 6 bits can represent:

`2^6 = 64`

different values.

This gives Base64 exactly 64 possible values that can be mapped to its 64-character alphabet.

The basic process is:

1. Convert the original data into bytes.
2. Represent those bytes as binary.
3. Divide the binary data into groups of 6 bits.
4. Convert each 6-bit value into a Base64 character.
5. Add padding when required.

### Example

During this project, I encoded:

`Hello Yemisi`

into Base64:

`SGVsbG8gWWVtaXNp`

The CLI was also able to decode the value back to:

`Hello Yemisi`

This demonstrates that Base64 is reversible and does not require an encryption key.

### Base64 Padding

Base64 commonly uses the `=` character as padding.

Depending on the input, an encoded value may end with:

`=`

or:

`==`

Padding helps complete the required Base64 output structure when the input does not divide evenly into the required groups.

However, the presence of `=` alone should not be used to conclude that something is Base64.

### Recognising Base64

Some indicators that a string may be Base64 include:

- Characters mainly from `A-Z`, `a-z`, `0-9`, `+` and `/`
- A length commonly divisible by 4
- Possible `=` or `==` padding at the end
- Decoding produces meaningful or structured data

These are indicators rather than absolute proof.

This is why this project uses **detection and confidence scoring** rather than assuming every Base64-looking string is definitely Base64.

> **Analyst takeaway:** Base64 can make data less readable, but it does not make the data confidential. If suspicious data looks Base64-encoded, decoding it may reveal useful information for further investigation.

## 4. Base32 Encoding

Base32 is an encoding method that represents binary data using a set of 32 printable characters.

The standard Base32 alphabet uses:

- Uppercase letters: `A-Z`
- Numbers: `2-7`
- The `=` character may be used for padding

### How Base32 Works

Base32 processes binary data in groups of **5 bits**.

Why 5 bits?

`2^5 = 32`

This means each 5-bit value can be mapped to one of the 32 characters in the Base32 alphabet.

The basic process is:

1. Convert the original data into bytes.
2. Represent the bytes as binary.
3. Divide the binary data into groups of 5 bits.
4. Map each group to a Base32 character.
5. Add padding when required.

### Base32 vs Base64

| Base32 | Base64 |
|---|---|
| Uses 32 characters | Uses 64 characters |
| Processes 5-bit groups | Processes 6-bit groups |
| Uses `A-Z` and `2-7` | Uses `A-Z`, `a-z`, `0-9`, `+`, `/` |
| Usually produces longer output | Usually produces shorter output |

### My Project Test

During testing, I encoded:

`Hello Yemisi`

using Base32.

I then decoded the generated value and successfully recovered:

`Hello Yemisi`

The tool's automatic detector also identified the encoded data as **Base32 with an 85% confidence score**.

### Padding

Base32 values may contain several `=` characters at the end.

During testing, I learned that preserving the correct padding is important. An incomplete Base32 value can cause decoding errors because the encoded data no longer has the expected structure.

### Recognising Base32

Possible indicators include:

- Primarily uppercase letters
- Numbers limited to `2-7`
- Possible `=` padding
- A structure consistent with Base32 encoding

These indicators are not enough on their own to guarantee that a value is Base32, which is why additional validation and confidence scoring are useful.

> **Analyst takeaway:** Base32 may appear in encoded identifiers, tokens, configuration data or other data being investigated. Recognising its character pattern can help an analyst determine the appropriate next step.

## 5. Hexadecimal Encoding

Hexadecimal, commonly called **Hex**, is a number system that uses 16 characters:

`0-9` and `A-F`

In computing, Hex provides a convenient way to represent binary data in a format that is easier for humans to read.

### How Hex Works

Binary data is made up of bits: `0` and `1`.

A group of **4 bits** can represent 16 possible values:

`2^4 = 16`

This means one hexadecimal character can represent 4 bits.

A byte contains 8 bits, so:

`1 byte = 2 hexadecimal characters`

For example:

`A` in ASCII has the decimal value `65`.

In hexadecimal:

`A → 41`

### My Project Test

During testing, I encoded:

`Hello Yemisi`

into Hex:

`48656c6c6f2059656d697369`

I then decoded the Hex value and successfully recovered:

`Hello Yemisi`

The automatic detector identified the value as **Hex with an 80% confidence score**.

### Why Hex Matters in Cybersecurity

Security analysts frequently encounter hexadecimal data when working with:

- Packet captures and network data
- Hex dumps
- File headers and file signatures
- Memory analysis
- Malware analysis
- Binary files
- Hash values

For example, viewing raw binary data directly can be difficult. Hex provides a more readable representation that allows analysts to inspect individual bytes.

### Recognising Hex

Possible indicators include:

- Characters limited to `0-9` and `A-F` (case-insensitive)
- An even number of characters when representing complete bytes
- Two hexadecimal characters commonly representing one byte

However, a string containing only hexadecimal characters is not automatically encoded data.

This became important when testing my tool because some strings can potentially match the characteristics of more than one encoding format.

The confidence-scoring system helps determine which format is the strongest candidate before decoding.

> **Analyst takeaway:** Learning to recognise Hex is important because it provides a human-readable representation of raw bytes frequently encountered during security investigations.

## 6. Base64URL Encoding

Base64URL is a URL-safe variation of standard Base64.

Standard Base64 uses characters such as:

`+` and `/`

These characters can have special meanings inside URLs. Base64URL therefore replaces them with URL-safe alternatives:

| Standard Base64 | Base64URL |
|---|---|
| `+` | `-` |
| `/` | `_` |

Padding using `=` may also be omitted in some Base64URL implementations.

### Why Base64URL Exists

Base64URL makes encoded binary data easier to use in URLs, web applications and other systems where standard Base64 characters may cause problems.

It is commonly associated with technologies such as:

- JSON Web Tokens (JWTs)
- Web applications
- APIs
- URL parameters
- Authentication and authorization data

### My Project Test

During testing, I encoded:

`Hello Yemisi`

using Base64URL and successfully decoded the result back to the original plaintext.

An interesting result occurred during automatic detection.

The tool identified my Base64URL test value as:

`Base64 — 95% confidence`

rather than Base64URL.

### Why Did This Happen?

For my specific test input, the resulting encoded value did not contain the special characters that distinguish Base64URL from standard Base64.

Therefore, the value was also structurally valid Base64.

This demonstrates an important limitation of automatic encoding detection:

> Different encoding formats can sometimes produce values that look identical.

A detector therefore cannot always determine the original encoding format from the encoded string alone.

### Security Analysis Relevance

For a security analyst, context is important.

If an encoded value appears inside a JWT, API request or URL parameter, Base64URL may be more likely even when the value also resembles standard Base64.

This means detection should combine:

`Pattern analysis + validation + confidence scoring + context`

rather than relying only on the appearance of the string.

> **Analyst takeaway:** Automatic detection is useful, but ambiguous data may require context before an analyst can confidently determine the encoding format.

## 7. URL / Percent Encoding

URL encoding, also known as **percent encoding**, is used to represent characters that may have a special meaning or may not be safe to use directly inside a URL.

Encoded characters are commonly represented using:

`%` followed by two hexadecimal digits.

### Example

A space can be represented as:

`%20`

During my project testing:

`Hello Yemisi`

was URL encoded as:

`Hello%20Yemisi`

The tool then successfully decoded the value back to:

`Hello Yemisi`

### How Percent Encoding Works

Characters can be represented using their byte values written in hexadecimal.

For example:

`Space → 20 → %20`

Other examples include:

| Character | URL Encoded |
|---|---|
| Space | `%20` |
| `!` | `%21` |
| `#` | `%23` |
| `%` | `%25` |

### Why URL Encoding Matters in Cybersecurity

Security analysts may encounter percent-encoded data while investigating:

- HTTP requests
- URLs and query parameters
- Web application logs
- API traffic
- Redirects
- Suspicious web activity

Encoding can also make parts of a URL or request less immediately readable.

For example:

`Hello Yemisi`

and:

`Hello%20Yemisi`

represent the same underlying text after decoding.

### Encoding Is Not Automatically Malicious

URL encoding is a normal and necessary part of web communication.

Its presence alone does not indicate an attack.

During an investigation, the important question is what the data reveals **after decoding and within its surrounding context**.

> **Analyst takeaway:** Percent-encoded values should sometimes be decoded during web-traffic analysis so that the analyst can inspect the underlying request or data more clearly.

## 8. Detecting Unknown Encodings

During a security investigation, an analyst may encounter an encoded value without knowing which encoding format was used.

Instead of manually trying several decoders, my tool includes a `detect` command that analyses the input and estimates the most likely encoding format.

### Confidence Scoring

The detector assigns confidence scores based on characteristics of the input.

During my testing, I observed results such as:

| Test | Detected Format | Confidence |
|---|---|---:|
| Base64 | Base64 | 95% |
| Base32 | Base32 | 85% |
| Hex | Hex | 80% |

A higher score means the input more strongly matches the characteristics expected for that encoding format.

### Why Confidence Scores Are Useful

Encoding detection is not always definite.

A string can sometimes satisfy the rules of more than one encoding format.

During my verbose recursive-decoding test, the outer layer produced:

| Candidate | Confidence | Decision |
|---|---:|---|
| Hex | 80% | Detected |
| Base64 | 50% | Below threshold |
| Base64URL | 0% | No match |
| Base32 | 0% | No match |
| URL | 0% | No match |

The tool selected Hex because it was the strongest candidate above the configured detection threshold.

After decoding that layer, the resulting value was analysed again and Base64 was detected with 95% confidence.

### Detection Threshold

The project uses a confidence threshold to help prevent weak matches from automatically being treated as valid encoding layers.

Conceptually:

`Candidate score → Compare with threshold → Decode only if sufficiently confident`

This is important because automatically decoding every possible match could produce incorrect results.

### Ambiguous Encodings

Some formats can overlap.

For example, during my Base64URL test, the encoded value was detected as standard Base64 because the particular output did not contain the `-` or `_` characters that would clearly distinguish Base64URL.

This showed me that automatic detection has limitations.

The appearance of data alone may not always reveal exactly how it was originally encoded.

### False Positives

During recursive peeling, I also encountered a case where the readable text:

`Security Analysis Demo`

was considered another possible Base64 layer.

The tool therefore attempted to continue decoding even though the intended plaintext had already been recovered.

For my controlled two-layer test, I used:

`--max-depth 2`

to restrict peeling to the two layers I had intentionally created.

This demonstrated why stopping conditions, confidence thresholds and analyst judgement are important when automatically processing unknown data.

> **Analyst takeaway:** Encoding detection should be treated as an informed assessment rather than absolute proof. Confidence scores, validation and surrounding context all help an analyst decide whether decoding a value makes sense.

## 9. Multi-Layer Encoding & Recursive Peeling

Data does not have to be encoded only once.

Multiple encoding methods can be applied one after another, creating several layers around the original data.

This can make the underlying content less immediately recognisable during analysis.

### Chained Encoding

My tool includes a `chain` feature that applies multiple encoding formats in sequence.

During testing, I created the following chain:

`Security Analysis Demo → Base64 → Hex`

The first step converted the plaintext into Base64.

The Base64 output was then encoded again using Hex.

The final value therefore could not be returned directly to the original plaintext using only one decoding step.

### Why Decoding Order Matters

Encoding layers must be removed in the reverse order in which they were applied.

If the encoding process is:

`Plaintext → Base64 → Hex`

then decoding must follow:

`Hex → Base64 → Plaintext`

This is similar to placing an item inside one box and then placing that box inside another box.

To reach the original item, the outer box must be opened first.

### Recursive Peeling

The `peel` feature automates this process.

Instead of requiring me to manually identify and decode every layer, the tool:

1. Analyses the current input.
2. Determines the strongest encoding candidate.
3. Decodes that layer.
4. Analyses the decoded result again.
5. Repeats the process until the stopping condition is reached.

During my controlled test, the tool identified:

`Layer 1 → Hex — 80% confidence`

followed by:

`Layer 2 → Base64 — 95% confidence`

and successfully recovered:

`Security Analysis Demo`

### Maximum Peeling Depth

Recursive decoding needs a stopping mechanism.

The tool provides the `--max-depth` option, which limits the maximum number of layers that can be removed.

For my two-layer test, I used:

`--max-depth 2`

This ensured that processing stopped after the two encoding layers I had intentionally created.

### Why This Matters in Security Analysis

Layered encoding can be used to make data harder to inspect quickly.

An analyst may therefore need to:

`Identify → Decode → Re-analyse → Decode again → Inspect final content`

Automating part of this process can make initial analysis faster, while the analyst still needs to validate whether the final result makes sense.

> **Analyst takeaway:** Recursive decoding is useful for investigating layered or obfuscated data, but automatic detection should have sensible stopping conditions to reduce the risk of over-decoding.

## 10. Applying This as a Security Analyst

The purpose of this project is not simply to encode and decode text. It demonstrates a workflow that can support the initial analysis of unfamiliar or suspicious encoded data.

### Example Investigation Workflow

If I encountered an unfamiliar encoded value during an investigation, I could approach it as follows:

1. **Observe the data**  
   Look at the structure, character set, length and surrounding context.

2. **Detect the possible encoding**  
   Use the tool to compare the value against supported encoding formats.

3. **Review the confidence score**  
   A high confidence score provides evidence of a likely match, but it should not be treated as absolute proof.

4. **Decode the value**  
   Examine what the encoded data contains.

5. **Check for additional layers**  
   If the decoded result still appears encoded, analyse it again or use recursive peeling.

6. **Inspect the final content**  
   Determine whether the recovered data is expected, suspicious or requires further investigation.

### Example From My Testing

I created:

`Security Analysis Demo → Base64 → Hex`

When analysing the final value, the tool identified:

`Hex (80%) → Base64 (95%) → Security Analysis Demo`

This demonstrated how an analyst could work backwards through multiple layers of encoded data.

### Analyst Judgement Still Matters

The tool assists with identifying and decoding data, but it does not determine whether the content itself is malicious.

An encoded value may be completely legitimate.

Likewise, successfully decoding a suspicious value is only one part of an investigation. The analyst would still need to consider where the data came from, what generated it, what system or user was involved, and what activity occurred around it.

> **Analyst takeaway:** Tools can accelerate analysis, but their output must be interpreted alongside context and other evidence.

## 11. What I Learned From This Project

Building and testing this tool helped me understand encoding from both a technical and security-analysis perspective.

Some of my main lessons were:

- **Encoding is not encryption.** Encoded data can be reversed without a secret key.
- **Different formats have different structures.** Base64, Base32, Hex, Base64URL and URL encoding each represent data differently.
- **Padding matters.** During Base32 testing, incorrect or incomplete padding caused decoding errors.
- **Detection is not always absolute.** Some strings can match more than one encoding format.
- **Context matters.** My Base64URL test was detected as Base64 because the output did not contain characters that clearly distinguished the two formats.
- **Confidence scoring helps manage uncertainty.** The tool compares possible formats rather than assuming the first match is correct.
- **Encoding layers must be removed in reverse order.** Data encoded as `Base64 → Hex` must be decoded as `Hex → Base64`.
- **Recursive decoding needs stopping conditions.** I encountered a false positive where readable text was treated as another possible encoding layer, which demonstrated the importance of thresholds and `--max-depth`.
- **Tool output still requires analyst judgement.** Successfully decoding data does not automatically mean the content is malicious.

Overall, this project helped me move beyond simply using encoding commands to understanding how encoded and layered data can be approached during security analysis.

## 12. Test Your Understanding

After completing this project, I should be able to answer the following questions:

1. What is the difference between encoding and encryption?
2. Why does Base64 use 6-bit groups?
3. Why can Base64URL sometimes be detected as standard Base64?
4. What does padding such as `=` or `==` do?
5. How can you recognise possible Hex data?
6. Why is confidence scoring useful when detecting an unknown encoding?
7. If data is encoded as `Base64 → Hex`, in what order should it be decoded?
8. What does recursive peeling mean?
9. Why does recursive decoding need a stopping condition such as `--max-depth`?
10. Why should an analyst not assume that encoded data is malicious?

### Practical Challenge

Given an unknown encoded value:

- Identify possible encoding formats.
- Compare the detection confidence scores.
- Decode the strongest candidate.
- Check whether another encoding layer exists.
- Continue only while the results remain valid and meaningful.
- Analyse the final content within its security context.



