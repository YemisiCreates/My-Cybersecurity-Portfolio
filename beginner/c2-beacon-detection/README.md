
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

The C2 Beacon Detector is a Python-based defensive network-analysis project designed to identify periodic outbound communication patterns that may indicate Command-and-Control (C2) beaconing.

The project generates synthetic network telemetry and analyses connection timing to identify recurring communication patterns. It also introduces jitter to demonstrate how timing variation can affect detection accuracy and produce false negatives when detection thresholds are too strict.

The project focuses on behavioural detection rather than relying solely on known malicious IP addresses, domains, or signatures.


### Detection Flow

                Simulated Traffic
                         ↓
                  Network Events
                         ↓
                 Interval Analysis
                         ↓
               Periodicity Detection
                         ↓
                   Risk Scoring
                         ↓
               Severity Classification
                         ↓
                 SOC Alert Generation
                         ↓
                Analyst Investigation

Example:

```ruby
Source:       192.168.1.25
Destination:  203.0.113.50
Port:         443

30 sec → 30 sec → 30 sec → 30 sec
                         ↓
              Periodic pattern identified
                         ↓
                 Risk Score: 100/100
                         ↓
                  Severity: High
                         ↓
              C2 Detection Alert
```


## How It Works
The project uses five main Python components:
1. **Traffic Simulation - 'simulator.py'**
   Generates synthetic network-event records representing repeated outbound communication. It supports configurable timing intervals and jitter.
2. **Interval Analysis - 'analyser.py'**
   Loads the synthetic telemetry, calculate the time between connections, measures interval consistency, and determines whether the communication is periodic.
3. **Risk Scoring - 'scoring.py'**
   Converts the detection result and interval consistency into a simple lab risk score from 0-100 and assigns a severity level.
4. **SOC Alert Generation - 'alert.py'**
   Formats the detection result into a SOC-style alert containing the source, destination, risk score, severity, average interval, and consistency.
5. **Pipeline Integration - 'main.py'**
   Connects the analyser, scoring, and alerting components so the full detection workflow can be run from one command.

### End-to-End Workflow
```text
            Synthetic Network Telemetry
                         ↓
                    analyzer.py
                         ↓
               Periodicity Detection
                         ↓
                     scoring.py
                         ↓
              Risk Score + Severity
                         ↓
                      alert.py
                         ↓
                  SOC-Style Alert
```

 Run the full analysis pipeline with
```bash
python3 -m src.main
```

Example output:

```text
=== C2 BEACON DETECTION ALERT ===
Detection: Possible C2 Beaconing
Detected: True
Risk Score: 100/100
Severity: High
Source: 192.168.1.25
Destination: 203.0.113.50:443
Average Interval: 30.14 seconds
Interval Consistency: 100.0%
```
              
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

---

### 5. SOC-Style C2 Detection Alert

![SOC-Style C2 Detection Alert](evidence/05-soc-c2-detection-alert.png)

**Analyst Observation:**  

The completed detection pipeline identified periodic outbound communication and generated a structured alert containing the affected source, destination, risk score, severity, average connection interval, and interval consistency.

**Security Relevance:**  

Transforming detection results into a structured alert makes the output more useful for SOC triage. Instead of receiving only a `True` or `False` result, an analyst receives contextual information that can help determine the severity of the detection and guide further investigation.

> **Analyst Note:** The `High` severity represents the project's lab-based scoring logic and does not independently confirm malicious activity.

**Security Relevance:**  

This demonstrates an important detection-engineering limitation: overly strict thresholds can miss beacon-like behaviour when communication intervals vary, creating a potential **false negative**.

The detection tolerance can therefore be adjusted to balance:

`Detection Sensitivity ↔ False Positives ↔ False Negatives'


## Detection Engineering Analysis

The testing demonstrated that periodicity can be useful for identifying beacon-like network behaviour, but detection accuracy depends heavily on the configured timing tolerance.

A strict tolerance successfully identifies highly regular communication but may fail when jitter is introduced, increasing the risk of false negatives. Increasing the tolerance may improve detection of jittered beaconing but can also increase false positives from legitimate periodic traffic.

This creates an important detection-engineering trade-off:

`Higher Sensitivity ↔ More False Positives`

`Lower Sensitivity ↔ More False Negatives`

For this reason, periodicity should be treated as one behavioural signal rather than standalone proof of malicious C2 activity.

### Alert Scoring and Prioritisation

The project extends the periodicity detection by converting the detection result and interval consistency into a numerical risk score and severity classification.

This provides an additional prioritisation layer for the analyst. Highly consistent periodic behaviour produces a higher score, while weaker or absent periodicity produces a lower score.

The scoring model is intentionally simple and designed for this controlled lab environment. In a production SOC, alert severity should incorporate additional contextual signals such as endpoint activity, threat intelligence, asset criticality, destination reputation, process behaviour, and other correlated security events.

Therefore, the risk score should be interpreted as an **alert-prioritisation mechanism**, rather than a probability that malicious C2 activity has occurred.

## MITRE ATT&CK Mapping

This project demonstrates detection concepts associated with the **Command and Control (C2)** stage of adversary activity.

| ATT&CK | Mapping | Relevance to This Project |
|---|---|---|
| **TA0011** | Command and Control | The project models and analyses repeated outbound communication patterns that may indicate C2 beaconing behaviour. |

### Mapping Scope

The current implementation focuses on **behavioural indicators of potential C2 communication**, particularly recurring outbound connections and timing periodicity.

The project does not currently inspect or validate specific application-layer protocols such as HTTP, HTTPS, or DNS. Therefore, a specific application-layer ATT&CK technique is not asserted solely because the simulated traffic uses destination port 443.

Future development could extend the detector with protocol-aware telemetry, allowing more specific ATT&CK technique mapping where supported by the observed behaviour.

### Detection Perspective

Rather than relying solely on known malicious IP addresses or signatures, this project uses **behaviour-based detection**.

The detector examines:

- repeated outbound connections
- source and destination relationships
- connection timestamps
- communication intervals
- periodicity
- timing variation (jitter)

This demonstrates how suspicious beacon-like behaviour can be identified using communication patterns even when a known malicious indicator is not available.

> **Analyst Note:** Periodic communication alone does not confirm malicious C2 activity. In a real SOC environment, an alert would require additional investigation and correlation with endpoint, DNS, process, authentication, and other network telemetry.


## SOC Investigation Workflow

A periodic beacon detection should be treated as a **starting point for investigation**, not immediate confirmation of compromise.

If this detection generated an alert in a SOC environment, I would follow the investigation process below:

### 1. Triage the Alert

Review the detection details to understand:

- Source IP / affected host
- Destination IP
- Destination port
- Connection frequency
- Number of repeated connections
- Time period over which the activity occurred
- Detection confidence and configured tolerance

**Goal:** Determine what triggered the alert and whether the behaviour warrants further investigation.

### 2. Validate the Network Activity

Examine additional network telemetry such as:

- Firewall logs
- Proxy logs
- DNS queries
- NetFlow/network flow data
- IDS/IPS alerts

Check whether the destination is expected for the affected system and whether similar communication occurs elsewhere in the environment.

### 3. Enrich the Destination

Investigate the destination IP or domain using available threat-intelligence sources.

Look for:

- Reputation
- Previous malicious activity
- Domain age
- Related indicators of compromise (IOCs)
- Known malware or C2 infrastructure associations

A clean reputation would **not automatically make the activity benign**, particularly when behavioural evidence remains suspicious.

### 4. Correlate With Endpoint Activity

Review EDR or endpoint telemetry from the source host.

Investigate:

- Which process initiated the connection?
- Is the process expected?
- What user account executed it?
- Are there suspicious parent/child process relationships?
- Are there persistence mechanisms?
- Are there unusual files or command-line activity?

This helps connect the **network behaviour** to activity occurring on the endpoint.

### 5. Scope the Activity

Determine whether the behaviour affects only one host or multiple systems.

Search for:

- Other hosts contacting the same destination
- Similar beacon intervals
- Related domains or IP addresses
- Similar endpoint processes
- Additional alerts associated with the same host or user

### 6. Determine the Disposition

Based on the collected evidence, classify the alert appropriately.

Possible outcomes include:

- **True Positive** — malicious C2 activity is supported by additional evidence.
- **False Positive** — legitimate software or expected network behaviour explains the periodic communication.
- **Suspicious / Inconclusive** — additional investigation or escalation is required.

### 7. Respond and Document

If malicious activity is confirmed, follow the organisation's incident-response procedures, which may include host isolation, blocking malicious infrastructure, preserving evidence, and escalation.

Document:

- Detection details
- Investigation queries
- Evidence reviewed
- Timeline
- Indicators discovered
- Analyst assessment
- Actions taken
- Final disposition

> **SOC Analyst Principle:** A beacon detection is an indicator for investigation. Periodicity provides behavioural evidence, but additional network and endpoint context is required before determining that Command-and-Control activity has occurred.


## Skills Demonstrated

- Network traffic analysis
- C2 beacon detection
- Python security automation
- Detection engineering
- Behaviour-based threat detection
- Security event investigation
- MITRE ATT&CK mapping
- SOC alert triage methodology
- Linux/macOS command-line usage
- Git and GitHub version control
- Technical cybersecurity documentation

## Alert Logging

The detector includes JSON-based alert logging to preserve detection results for later analysis.

When the detection pipeline identifies beacon-like behaviour, the alert can be written to:

```text
logs/alerts.json
```

Each alert contains structured fields such as:

- Timestamp
- Detection name
- Detection status
- Risk score
- Severity
- Source IP
- Destination IP and port
- Average connection interval
- Interval consistency

Example alert:

```json
{
  "timestamp": "2026-08-22T20:55:09.976486",
  "detection": "Possible C2 Beaconing",
  "detected": true,
  "risk_score": 100,
  "severity": "High",
  "source_ip": "192.168.1.25",
  "destination_ip": "203.0.113.50",
  "destination_port": 443,
  "average_interval_seconds": 30.14,
  "interval_consistency_percent": 100.0
}
```

### Security Relevance

Structured alert logging makes detection results easier to preserve, review, and process programmatically. In a SOC environment, structured security events may be forwarded to monitoring or SIEM platforms for correlation with other telemetry.

The generated `logs/` directory is excluded from version control through `.gitignore` so runtime alert data is not committed to the repository.


## Automated Testing

The project uses `pytest` to validate core detection and logging behaviour.
## Alert Logging

The detector includes JSON-based alert logging to preserve detection results for later analysis.

When the detection pipeline identifies beacon-like behaviour, the alert can be written to:

```text
logs/alerts.json
```

Each alert contains structured fields such as:

- Timestamp
- Detection name
- Detection status
- Risk score
- Severity
- Source IP
- Destination IP and port
- Average connection interval
- Interval consistency

Example alert:

```json
{
  "timestamp": "2026-08-22T20:55:09.976486",
  "detection": "Possible C2 Beaconing",
  "detected": true,
  "risk_score": 100,
  "severity": "High",
  "source_ip": "192.168.1.25",
  "destination_ip": "203.0.113.50",
  "destination_port": 443,
  "average_interval_seconds": 30.14,
  "interval_consistency_percent": 100.0
}
```

### Security Relevance

Structured alert logging makes detection results easier to preserve, review, and process programmatically. In a SOC environment, structured security events may be forwarded to monitoring or SIEM platforms for correlation with other telemetry.

The generated `logs/` directory is excluded from version control through `.gitignore` so runtime alert data is not committed to the repository.


## Automated Testing

The project uses `pytest` to validate core detection and logging behaviour.
Test files:

- [`tests/test_detector.py`](tests/test_detector.py) — validates beacon detection, irregular traffic handling, insufficient data, risk scoring, and severity classification.
- [`tests/test_logger.py`](tests/test_logger.py) — validates that structured detection alerts are successfully written to JSON.


The automated tests currently verify:

- Regular intervals trigger beacon detection
- Irregular intervals do not trigger beacon detection
- Insufficient interval data does not trigger detection
- High interval consistency produces a high-severity result
- No detection produces a zero risk score
- Detection alerts can be written successfully as JSON

Run the complete test suite with:

```bash
python3 -m pytest tests/ -v
```

Current test result:

```text
6 passed
```

Automated testing helps ensure that changes to the project do not unintentionally break existing detection, scoring, or logging behaviour.


## Ethical Use

This project was developed strictly for educational and defensive cybersecurity purposes in a controlled local lab environment.


