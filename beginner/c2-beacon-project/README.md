# C2 Beacon Security Analysis Project

## Overview
This project was completed as part of my cybersecurity learning journey to understand Command-and-Control (C2) beaconing techniques, detection methods, and MITRE ATT&CK mappings.

The project explored how beacon implants communicate with operator servers using WebSockets, encoded traffic, heartbeat intervals, jitter, and asynchronous task queues.

---

## What I Learned

- Command-and-Control (C2) infrastructure basics
- MITRE ATT&CK techniques related to beaconing
- WebSocket communication concepts
- XOR + Base64 traffic obfuscation
- Heartbeat intervals and jitter
- Beacon reconnection and exponential backoff
- Beacon detection techniques used by defenders
- Docker-based application deployment
- Troubleshooting frontend/backend dependency issues

---

## Key Security Concepts

### Beacon Jitter
Beacon jitter randomizes callback timing to make malicious traffic harder to detect through predictable intervals.

### XOR Encoding
XOR encoding is a lightweight obfuscation technique often used in malware communications but is not considered strong encryption.

### Detection Opportunities
Defenders can detect beaconing by monitoring:

- Periodic network traffic patterns
- Suspicious WebSocket connections
- Encoded payloads
- Process spawning behavior
- Beacon persistence mechanisms

---

## Tools & Technologies

- Docker
- Python
- FastAPI
- React
- WebSockets
- MITRE ATT&CK
- SQLite
- TypeScript

---

## Challenges Faced

While working on this project, I encountered several real-world troubleshooting issues including:

- Docker installation compatibility issues
- Missing environment configuration files
- Package dependency conflicts
- Frontend build failures using pnpm
- Backend README build validation errors

Troubleshooting these issues improved my understanding of development environments and security tooling setup.

---

## Screenshots / Notes

I reviewed the learning modules included in the project and explored:

- C2 framework architecture
- Beacon communication flows
- ATT&CK technique mapping
- Defensive detection strategies
- Security tradeoffs in beacon design

---

## Skills Demonstrated

- Cybersecurity research
- Security operations concepts
- Threat detection awareness
- Technical troubleshooting
- Linux/macOS terminal usage
- GitHub project documentation

---

## Disclaimer

This project was used strictly for educational and defensive cybersecurity learning purposes in a local lab environment.


