# 🛡️ Network Intrusion Detection System — CodeAlpha Internship

![Snort](https://img.shields.io/badge/Snort-2.9.20-red?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Operational-green?style=flat-square)
![Internship](https://img.shields.io/badge/CodeAlpha-Cybersecurity%20Internship-purple?style=flat-square)

## 📋 Overview

This project implements a **Network-Based Intrusion Detection System (NIDS)** using **Snort 2.9.20** on Windows. The system monitors live network traffic in real time, applies custom detection rules, and generates alerts when suspicious activity is detected.

This was completed as **Task 4** of the CodeAlpha Cybersecurity Internship Program.

---

## 🔧 Tools & Technologies

| Tool          | Version      | Purpose                         |
|---------------|--------------|---------------------------------|
| Snort         | 2.9.20-WIN64 | Core IDS engine                 |
| Npcap         | Latest       | Packet capture driver (Windows) |
| Windows 10/11 |       —      | Host operating system           |
| PowerShell    | Built-in     | Real-time alert monitoring      |

---

## 📁 Repository Structure

```
CodeAlpha_NetworkIDS/
├── snort.conf          # Production-ready Snort configuration
├── local.rules         # Custom detection rules
├── screenshots/        # Evidence of live detections
│   ├── snort_running.png
│   ├── icmp_alerts.png
│   ├── tcp_alerts.png
│   └── alert_log.png
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites

1. **Npcap** — Download and install from https://npcap.com/#download
   - ✅ Check "Install Npcap in WinPcap API-compatible Mode" during installation

2. **Snort 2.9.x for Windows** — Download from https://www.snort.org/downloads

### Installation Steps

```bash
# 1. Install Snort to C:\Snort (default path — do not change)

# 2. Create required directories
mkdir C:\Snort\log

# 3. Create whitelist/blacklist files (required by Snort)
echo # white list > C:\Snort\rules\white_list.rules
echo # black list > C:\Snort\rules\black_list.rules

# 4. Copy local.rules to C:\Snort\rules\local.rules
```

### Key Configuration Changes in snort.conf

```bash
# Set your network
var HOME_NET 192.168.x.0/24
var RULE_PATH C:\Snort\rules

# Fix Windows dynamic library paths
dynamicpreprocessor directory C:\Snort\lib\snort_dynamicpreprocessor
dynamicengine C:\Snort\lib\snort_dynamicengine\sf_engine.dll

# Disable active responses (not supported in passive mode)
max_active_responses 0

# Enable VLAN-agnostic mode (required for most Windows network adapters)
config vlan_agnostic

# Include custom rules
include C:\Snort\rules\local.rules
```

### Validate Configuration

```bash
C:\Snort\bin\snort.exe -c C:\Snort\etc\snort.conf -T
# Expected: Snort successfully validated the configuration!
```

---

## 📏 Detection Rules

The file `local.rules` contains 4 custom detection rules:

```
# Rule 1: Detect ICMP Ping (network reconnaissance)
alert icmp any any -> any any (msg:"[IDS] ICMP Ping Detected"; sid:1000001; rev:2;)

# Rule 2: Detect HTTP Traffic on port 80
alert tcp any any -> any 80 (msg:"[IDS] HTTP Traffic Detected"; flow:to_server,established; sid:1000002; rev:2;)

# Rule 3: Detect SSH Connection Attempts
alert tcp any any -> any 22 (msg:"[IDS] SSH Connection Attempt"; sid:1000003; rev:2;)

# Rule 4: Detect TCP Traffic (established sessions)
alert tcp any any -> any any (msg:"[IDS] TCP Traffic Detected"; flow:established; sid:1000004; rev:2;)
```

### Rule Anatomy

```
alert  tcp    any  any  ->  any  80   (msg:"..."; sid:1000002; rev:2;)
  │     │      │    │        │    │     │               │          │
  │     │      │    │        │    │     └─ alert message │          └─ revision
  │     │      │    │        │    └─ destination port    └─ unique rule ID
  │     │      │    │        └─ destination IP
  │     │      │    └─ source port
  │     │      └─ source IP
  │     └─ protocol
  └─ action
```

---

## 🚀 Running the IDS

### Step 1 — Find your network interface number

```bash
# Try interfaces 1, 2, 3... until you see packets flowing
C:\Snort\bin\snort.exe -v -i 1
```

### Step 2 — Launch Snort IDS (Terminal 1)

```bash
C:\Snort\bin\snort.exe -c C:\Snort\etc\snort.conf -l C:\Snort\log -A fast -i 5
```

### Step 3 — Monitor alerts in real time (Terminal 2)

```bash
powershell Get-Content C:\Snort\log\alert.ids -Wait
```

### Step 4 — Generate test traffic (Terminal 3)

```bash
# Trigger Rule 1 — ICMP
ping 8.8.8.8

# Trigger Rule 2 — HTTP
curl http://example.com

# Trigger Rule 3 — SSH
powershell Test-NetConnection -ComputerName 192.168.1.1 -Port 22
```

---

## 📊 Sample Alert Output

```
05/28-17:44:12.123456  [**] [1:1000001:2] [IDS] ICMP Ping Detected [**]
[Priority: 0] {ICMP} 192.168.1.10 -> 8.8.8.8

05/28-17:44:15.654321  [**] [1:1000004:2] [IDS] TCP Traffic Detected [**]
[Priority: 0] {TCP} 192.168.1.10:52301 -> 93.184.216.34:80
```

---

## 🐛 Troubleshooting (Windows-Specific)

| Issue | Cause | Fix |
|-------|-------|-----|
| `Could not stat dynamic module path` | Linux paths in snort.conf | Replace with `C:\Snort\lib\...` paths |
| `Unable to open address file white_list.rules` | Missing files | Create empty whitelist/blacklist files |
| `Active response: can't open ip` | Active response enabled | Set `max_active_responses 0` |
| No alerts despite traffic | Wrong interface or VLAN tagging | Use `-i X` flag + add `config vlan_agnostic` |
| `alert` file not found | Wrong extension on Windows | Use `alert.ids` instead of `alert` |

---

## 📚 Concepts Covered

- **Network packet capture** using Npcap on Windows
- **Snort rule syntax** — action, protocol, IP/port matching, rule options
- **IDS vs Firewall** — passive monitoring vs active blocking
- **VLAN-aware packet inspection** on Windows network adapters
- **Real-time alert monitoring** and log file analysis
- **OWASP-aligned thinking** — detection before response

---

## 👤 Author

**CodeAlpha Cybersecurity Internship**
Task 4 — Network Intrusion Detection System

---

*Built and configured from scratch on Windows — including full debugging of Snort's Windows-specific configuration challenges.*
