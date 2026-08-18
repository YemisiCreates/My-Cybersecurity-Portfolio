# C2 Beacon Detection & SOC Investigation Lab

A defensive cybersecurity project that simulates Command-and-Control (C2) beacon traffic and detects periodic network communication that may indicate beaconing behaviour.

This project focuses on the SOC analyst perspective: generating safe synthetic telemetry, analysing connection timing, identifying periodic communication, testing the impact of jitter, and improving detection logic to reduce false negatives.

## Project Goal

The goal of this project is to understand how C2 beaconing can appear in network telemetry and how a SOC analyst can detect suspicious periodic communication without relying only on known malicious indicators.

The project currently:

- Generates synthetic network events
- Simulates repeated outbound connections
- Calculates connection intervals
- Detects highly periodic communication
- Introduces timing jitter
- Demonstrates how jitter can cause a false negative
- Adjusts detection tolerance to recognise jittered beaconing

## How It Works

The project follows a simple detection pipeline:

1. **Traffic Simulation**  
   `simulator.py` generates synthetic outbound network connections representing C2-style beacon traffic.

2. **Telemetry Generation**  
   Each event contains a timestamp, source IP, destination IP, and destination port.

3. **Interval Analysis**  
   `analyzer.py` calculates the time difference between consecutive network connections.

4. **Periodicity Detection**  
   The detector compares the connection intervals to determine whether communication is occurring at a consistent pattern.

5. **Jitter Testing**  
   Random timing variation is introduced to simulate more realistic beacon behaviour and test whether the detector can still identify the pattern.

6. **Detection Result**  
   The analyzer returns a result such as:

   `Periodic beacon detected: True`
## Security Analysis & Learning Outcomes

Through this project, I explored:

- C2 (Command and Control) communication architecture
- Periodic beaconing behaviour and network traffic patterns
- Detection of suspicious timing intervals in network events
- MITRE ATT&CK concepts associated with Command and Control activity
- Defensive detection strategies for identifying beacon-like behaviour
- The effect of jitter on beacon detection and potential false negatives
- Security trade-offs between detection sensitivity and false positives

## Skills Demonstrated

- Network traffic analysis
- C2 beacon detection
- Python-based security automation
- Detection engineering fundamentals
- Security event analysis
- Threat detection and investigation
- Technical troubleshooting
- Linux/macOS command-line usage
- Git and GitHub version control
- Cybersecurity documentation

## Ethical Use

This project was developed strictly for educational and defensive cybersecurity purposes in a controlled local lab environment.
