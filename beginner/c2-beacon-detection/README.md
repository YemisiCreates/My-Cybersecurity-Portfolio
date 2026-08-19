
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

## Overview

The C2 Beacon Detector is a defensive network-analysis project that identifies periodic outbound communication patterns that may be associated with Command-and-Control (C2) beaconing.

The project currently:

- Generates synthetic network connection telemetry for safe analysis.
- Simulates repeated outbound communication between a source and destination.
- Calculates the time interval between consecutive connections.
- Detects highly periodic communication patterns.
- Introduces **jitter** to simulate variation in beacon timing.
- Tests how jitter affects detection accuracy.
- Demonstrates how overly strict detection thresholds can create **false negatives**.
- Allows detection sensitivity to be adjusted using a timing tolerance.

### Detection Flow

`Simulated Traffic → Network Events → Interval Analysis → Periodicity Check → Detection Result`

Example:

```ruby
Source:       192.168.1.25
Destination:  203.0.113.50
Port:         443

30 sec → 30 sec → 30 sec → 30 sec
                         ↓
              Periodic pattern identified
                         ↓
          Periodic beacon detected: True
```


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

```text
Periodic beacon detected: True
```

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

## Detection Evidence

### 1. Periodic Beacon Detection

![Periodic Beacon Detected](evidence/01-periodic-beacon-detected.png)

**Analyst observation:**  
The detector identified repeated network connections occurring at consistent intervals, resulting in `Periodic beacon detected: True`.

**Security Relevance:**  

Consistent outbound communication intervals can be an indicator of automated C2 beaconing. In a real SOC investigation, this behaviour would warrant further analysis of the source host, destination IP, process activity, DNS activity, and surrounding network telemetry.

---

### 2. Connection Interval Analysis

![Interval Analysis](evidence/02-interval-analysis.png)

**Analyst Observation:**  

The connection timestamps were converted into intervals between consecutive network events. Similar intervals indicate that the communication is occurring on a predictable schedule.

**Security Relevance:**  

Interval analysis helps analysts distinguish potentially automated beaconing behaviour from less predictable user-generated network traffic.

---

### 3. Simulated Network Events

![Simulated Network Events](evidence/03-simulated-network-events.png)

**Analyst Observation:**  

Synthetic network telemetry was generated to provide a safe dataset containing repeated outbound connection events for analysis.

**Security Relevance:**  

Using synthetic telemetry allows detection logic to be developed and tested in a controlled environment without generating real malicious C2 traffic.

---

### 4. Jittered Traffic — No Beacon Detected

![Jittered Traffic No Beacon](evidence/04-jittered-traffic-no-beacon.png)

**Analyst Observation:**  

Timing variation (jitter) was introduced between network connections. The additional variation caused the communication pattern to fall outside the detector's configured tolerance.

**Security Relevance:**  

This demonstrates an important detection-engineering limitation: overly strict thresholds can miss beacon-like behaviour when communication intervals vary, creating a potential **false negative**.

The detection tolerance can therefore be adjusted to balance:

`Detection Sensitivity ↔ False Positives ↔ False Negatives'


