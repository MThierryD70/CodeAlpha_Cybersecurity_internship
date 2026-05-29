# 🔍 Task 1 — Basic Network Sniffer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Scapy](https://img.shields.io/badge/Library-Scapy-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

A real-time network packet sniffer built with Python and Scapy. Captures, analyzes, and logs live network traffic — displaying source/destination IPs, protocols, and services.

---

## 📋 Features

- Captures TCP, UDP, and ICMP packets in real time
- Identifies source and destination IP addresses and ports
- Maps port numbers to known services (HTTP, HTTPS, DNS, SSH, FTP...)
- Logs all captured packets with timestamps to `capture.log`
- Clean formatted console output

---

## 🧠 Concepts Covered

| Concept           | Description                                               |
|-------------------|-----------------------------------------------------------|
| Network layers    | Ethernet → IP → TCP/UDP → Payload                         |
| Packet sniffing   | Passive capture using Scapy's `sniff()`                   |
| Protocol analysis | Identifying TCP, UDP, ICMP from packet headers            |
| Well-known ports  | Mapping ports to services (80=HTTP, 443=HTTPS, 53=DNS...) |
| Event logging     | Timestamped persistent logs with Python `logging` module  |

---

## 🔧 Requirements

```bash
pip install scapy
```

Also requires **Npcap** (Windows packet capture driver):
👉 https://npcap.com/#download
> ✅ Check "Install Npcap in WinPcap API-compatible Mode" during installation

---

## 🚀 Usage

```bash
# Must run as Administrator
python sniffer.py
```

Generate traffic to see results:
```bash
ping 8.8.8.8          # ICMP packets
curl http://example.com  # HTTP packets
```

---

## 📊 Sample Output

```
═══════════════════════════════════════════════════════
   🛡️  Network Sniffer — CodeAlpha Internship
═══════════════════════════════════════════════════════
   Start time : 2026-05-28 17:30:00
   Logs saved : capture.log
═══════════════════════════════════════════════════════
[TCP] [HTTPS] 192.168.1.10:52301 ──▶ 142.250.74.46:443
[UDP] [DNS]   192.168.1.10:1085  ──▶ 8.8.8.8:53
[TCP] [HTTP]  192.168.1.10:49832 ──▶ 93.184.216.34:80
[ICMP] [PING] 192.168.1.10       ──▶ 8.8.8.8
✅ Capture complete. Check capture.log
```

---

## 📝 Log File Format

```
2026-05-28 17:30:01 | [TCP] [HTTPS] 192.168.1.10:52301 ──▶ 142.250.74.46:443
2026-05-28 17:30:02 | [UDP] [DNS] 192.168.1.10:1085 ──▶ 8.8.8.8:53
```

---

## 🗂️ File Structure

```
Task1_NetworkSniffer/
├── sniffer.py       # Main sniffer script
├── capture.log      # Generated log file (after running)
└── README.md
```

---

## ⚠️ Disclaimer

This tool is for educational purposes only. Only use on networks you own or have explicit permission to monitor.
