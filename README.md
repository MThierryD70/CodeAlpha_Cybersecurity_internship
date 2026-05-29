# 🛡️ CodeAlpha Cybersecurity Internship

![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Cybersecurity%20Internship-purple?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Snort](https://img.shields.io/badge/Snort-2.9.20-red?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Tasks-4%2F4%20Completed-green?style=flat-square)

Welcome to my CodeAlpha Cybersecurity Internship repository. This repo contains all 4 completed tasks covering network security, social engineering awareness, secure code auditing, and intrusion detection.

---

## 📁 Repository Structure

```
CodeAlpha_CyberSecurity_Internship/
│
├── Task1_NetworkSniffer/
│     └── sniffer.py                        # Python packet capture tool
│
├── Task2_PhishingAwareness/
│     └── phishing_awareness.html           # Interactive training module + quiz
│     └── phishing_quiz.html
│
├── Task3_SecureCodingReview/
│     └── Secure_Code_Audit_Report.docx     # Professional audit report
│
├── Task4_NetworkIDS/
│     ├── snort.conf                        # Production Snort configuration
│     ├── local.rules                       # Custom detection rules
│     └── screenshots/                      # Live detection evidence
│
└── README.md
```

---

## ✅ Tasks Overview

### Task 1 — Basic Network Sniffer 🔍

A Python-based network packet sniffer built with **Scapy** that captures and analyzes live network traffic in real time.

**Features:**
- Captures TCP, UDP, and ICMP packets
- Identifies source/destination IPs and ports
- Maps port numbers to known services (HTTP, HTTPS, DNS, SSH...)
- Logs all captured packets with timestamps to `capture.log`

**Tech:** Python, Scapy, Npcap, logging module

**Run:**
```bash
# Run as Administrator
python sniffer.py
```

---

### Task 2 — Phishing Awareness Training 🎣

An interactive HTML training module educating users about phishing attacks, social engineering, and best practices for protection.

**Contents:**
- 5 slides covering phishing types, psychological triggers, red flags, and defenses
- Interactive 5-question quiz with instant feedback and scoring
- Real-world examples of phishing emails

**Open in browser:** Just open `phishing_awareness.html` — no server needed.

---

### Task 3 — Secure Coding Review 🔐

A professional security audit report identifying and remediating 5 critical vulnerabilities across 3 Python/Flask code modules.

**Findings covered:**

| ID      | Vulnerability                 | Severity     | OWASP |
|---------|-------------------------------|--------------|-------|
| #001  | SQL Injection                 | CRITICAL     | A01   |
| #002a | Plaintext Password Storage    | CRITICAL     | A02   |
| #002b | Sensitive Data in Logs        | HIGH         | A03   |
| #003a | Reflected XSS                 | HIGH         | A03   |
| #003b | Debug Mode in Production      | CRITICAL     | A05   |

Each finding includes vulnerable code, proof of concept, and fixed code with explanation.

---

### Task 4 — Network Intrusion Detection System 🚨

A fully configured **Snort 2.9.20** IDS on Windows that monitors live network traffic and generates real-time alerts based on custom detection rules.

**Detection Rules:**
```
alert icmp any any -> any any        → Detects ICMP ping / network scans
alert tcp any any -> any 80          → Detects HTTP traffic
alert tcp any any -> any 22          → Detects SSH connection attempts
alert tcp any any -> any any         → Detects established TCP sessions
```

**Run:**
```bash
# Terminal 1 — Start IDS
C:\Snort\bin\snort.exe -c C:\Snort\etc\snort.conf -l C:\Snort\log -A fast -i 6

# Terminal 2 — Monitor alerts in real time
powershell Get-Content C:\Snort\log\alert.ids -Wait
```

**Key Windows challenges solved:**
- Dynamic library paths (Linux → Windows)
- VLAN-agnostic mode for Windows network adapters
- Active response disabled for passive monitoring mode
- Interface detection and alert file extension (`.ids`)

---

## 🧰 Technologies Used

| Technology              | Purpose                               |
|-------------------------|---------------------------------------|
| Python 3 + Scapy        | Network packet capture and analysis   |
| Snort 2.9.20            | Intrusion detection engine            |
| Npcap                   | Windows packet capture driver         |
| HTML / CSS / JavaScript | Interactive phishing awareness module |
| OWASP Top 10            | Secure coding review framework        |

---

## ⚠️ Disclaimer

All tools and techniques in this repository were used exclusively on personal machines and networks for educational purposes as part of the CodeAlpha Cybersecurity Internship. Never use these tools on systems or networks without explicit written permission.

---

## 👤 Author
**Thierry**
**CodeAlpha Cybersecurity Internship Program**  
All 4 tasks completed ✅
