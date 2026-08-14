# Overview

## What This Project Does

Base64tool is a Python command-line security utility for identifying, encoding,
decoding, and analysing data represented in multiple encoding formats,
including Base64, Base64URL, Base32, hexadecimal, and URL encoding.

The tool can automatically analyse unknown encoded strings, assign confidence
scores to possible encoding formats, and recursively decode multiple layers
until the original readable data is recovered.

This is particularly useful during security analysis because suspicious
payloads are not always presented as readable text. Encoding can be used to
obscure commands, URLs, scripts, or other data from immediate inspection.

## Why This Matters in Cybersecurity

Security analysts often encounter encoded data in logs, network traffic,
URLs, scripts, tokens, and suspicious payloads.

Encoding can also be used to make malicious content less obvious during
analysis. For example, an attacker may encode a command in Base64 and then
encode the result again in Hex or URL encoding.

During this project, I tested how b64tool can detect these formats,
assign confidence scores, and recursively remove multiple encoding layers
until the original readable content is recovered.

This makes the tool useful for quickly inspecting suspicious encoded data
during security investigations.
