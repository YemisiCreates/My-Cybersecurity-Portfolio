
```ruby
 ██████╗██████╗     ██████╗ ███████╗ █████╗  ██████╗ ██████╗ ███╗   ██╗
██╔════╝╚════██╗    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║
██║      █████╔╝    ██████╔╝█████╗  ███████║██║     ██║   ██║██╔██╗ ██║
██║     ██╔═══╝     ██╔══██╗██╔══╝  ██╔══██║██║     ██║   ██║██║╚██╗██║
╚██████╗███████╗    ██████╔╝███████╗██║  ██║╚██████╗╚██████╔╝██║ ╚████║
 ╚═════╝╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

```ruby
         ╔══════════════════════════════════════════════════════════════╗
         ║                     C2 BEACON DETECTOR                      ║
         ║                                                              ║
         ║              Detect • Analyse • Investigate                 ║
         ║                                                              ║
         ║                     CYBERSECURITY PROJECT                   ║
         ╚══════════════════════════════════════════════════════════════╝

                              GitHub: YemisiCreates
```
[![Cybersecurity Project](https://img.shields.io/badge/Cybersecurity-C2%20Beacon%20Detection-red?style=flat&logo=github)](https://github.com/YemisiCreates/My-Cybersecurity-Portfolio/tree/main/beginner/c2-beacon-detection) [![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org) [![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Command%20%26%20Control-ED1C24?style=flat)](https://attack.mitre.org/tactics/TA0011/) ![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-8A2BE2?style=flat) ![SOC Analysis](https://img.shields.io/badge/SOC-Analysis-0078D4?style=flat) ![Network Analysis](https://img.shields.io/badge/Network-Traffic%20Analysis-2EA44F?style=flat)
> A defensive cybersecurity project for detecting and analysing periodic Command-and-Control (C2) beaconing behaviour in simulated network traffic.

**This is a project overview — detection logic, analysis, evidence, and technical walkthroughs are documented below.**

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
