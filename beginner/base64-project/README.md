
```ruby
██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║
██████╔╝███████║███████╗█████╗  ███████╗ ███████║       ██║   ██║   ██║██║   ██║██║
██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║       ██║   ██║   ██║██║   ██║██║
██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
```
```ruby
╔══════════════════════════════════════════════════════════════╗
║                  BASE64 ENCODER • DECODER                   ║
║                                                              ║
║                    Encode • Decode • Convert                ║
║                                                              ║
║                     CYBERSECURITY PROJECT                   ║
╚══════════════════════════════════════════════════════════════╝

                 GitHub: Oluwayemisi-Teluwo
```
[![(Cybersecurity Projects](https://img.shields.io/badge/Cybersecurity--Projects-Yemisi%20base64-red?style=flat&logo=github)](https://github.com/YemisiCreates/My-Cybersecurity-Portfolio/tree/main/beginner/base64-project)
[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![License: AGPLv3](https://img.shields.io/badge/License-AGPL_v3-purple.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI](https://img.shields.io/pypi/v/b64tool?color=3775A9&logo=pypi&logoColor=white)](https://pypi.org/project/b64tool/)
> A Cybersecurity Tool for Detecting, Decoding and Analysing Layered Data

**This is a quick overview — security theory, architecture, and full walkthroughs are in the [learn modules](learn/).**

**[Screenshots & Demo →](DEMO.md)**
## What I Did
I used the b64tool cybersecurity CLI project to:
- Encode text
- Decode Base64 strings
- Detect encoding formats
- Peel encoding layers
- Chain encodings

## Quick Start
``` bash
uv tool install b64tool
b64tool encodes "Hello World"
```

> [!TIP]
> This project uses [`just`](https://github.com/casey/just) as a command runner. Type `just` to see all available commands.
>
> Install: `curl -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin`

## Commands
| Command | Description |
|---------|-------------|
| `b64tool encode` | Encode text into Base64, Base64URL, Base32, Hex, or URL format |
| `b64tool decode` | Decode encoded text back to plaintext |
| `b64tool detect` | Auto-detect the encoding format with confidence scoring |
| `b64tool peel` | Recursively strip multi-layered encoding to reveal original data |
| `b64tool chain` | Chain multiple encoding steps together for obfuscation testing |

## Learn
This project includes step-by-step learning materials covering security theory, architecture, and implementation.

| Module | Topic |
|--------|-------|
| [00 - Overview](learn/00-OVERVIEW.md) | Prerequisites and quick start |
| [01 - Concepts](learn/01-CONCEPTS.md) | Security theory and real-world breaches |
| [02 - Architecture](learn/02-ARCHITECTURE.md) | System design and data flow |
| [03 - Implementation](learn/03-IMPLEMENTATION.md) | Code walkthrough |
| [04 - Challenges](learn/04-CHALLENGES.md) | Detection limitations, false positives and lessons learned|

## Cybersecurity Relevance

Attackers can use encoding and multiple transformation layers to obscure commands, URLs, scripts and other payload data.

This project helped me understand how a security analyst can identify suspicious encoding, compare confidence scores, safely decode data and recursively analyse multiple layers. Testing also demonstrated the importance of validating automated detections because confidence-based analysis can produce false positives and unintended over-peeling.

## License

AGPL 3.0
