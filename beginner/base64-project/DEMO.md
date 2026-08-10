
# Demo & Preview

---

## Installation

```bash
uv tool install base64tool
```

---

## Encoding

```bash
base64tool encode "Hello World"
```

Output:

```text
SGVsbG8gV29ybGQ=
```

---

## Decoding

```bash
base64tool decode "SGVsbG8gV29ybGQ="
```

Output:

```text
Hello World
```

---

## Recursive Layer Detection

```bash
base64tool peel "VTBkV2JH..."
```

Output:

```text
Layer 1: Base64
Layer 2: URL encoding
Layer 3: Plain text
```
