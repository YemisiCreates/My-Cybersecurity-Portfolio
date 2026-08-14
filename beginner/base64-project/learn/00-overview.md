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
