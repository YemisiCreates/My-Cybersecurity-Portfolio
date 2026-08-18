## Detection Evidence

This folder contains evidence generated while testing the C2 beacon
detection workflow.

### 01 — Periodic Beacon Detected
Demonstrates detection of repeated network connections occurring at
consistent time intervals, a behavioural pattern commonly associated
with automated beaconing.

![Periodic Beacon Detected](01-periodic-beacon-detected.png)

### 02 — Interval Analysis
Shows the calculated time intervals between simulated network
connections used to determine whether communication is periodic.

![Interval Analysis](02-interval-analysis.png)

### 03 — Simulated Network Events
Shows the network-event dataset generated for analysis, including
timestamps and connection information used by the detector.

![Simulated Network Events](03-simulated-network-events.png)

### 04 — Jittered Traffic / No Beacon
Demonstrates how variation in connection timing can reduce periodicity
and prevent the traffic from meeting the beacon-detection threshold.

![Jittered Traffic — No Beacon](04-jittered-traffic-no-beacon.png)
