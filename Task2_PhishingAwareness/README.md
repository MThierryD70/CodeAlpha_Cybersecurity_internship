# 🎣 Task 2 — Phishing Awareness Training

![HTML](https://img.shields.io/badge/HTML-5-orange?style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square)
![No Server](https://img.shields.io/badge/Server-Not%20Required-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

An interactive phishing awareness training module built as a single HTML file. Covers phishing types, psychological manipulation tactics, red flags, and best practices — with an integrated 5-question quiz.

---

## 📋 Features

- **5 interactive slides** navigable with Previous/Next buttons
- **4 phishing types** explained with clickable cards
- **3 psychological triggers** attackers exploit (urgency, fear, greed)
- **6-item red flags checklist** for identifying phishing attempts
- **4 best practices** for protection
- **5-question interactive quiz** with instant feedback and final score
- No installation or server required — open directly in any browser

---

## 🧠 Concepts Covered

### The 4 Types of Phishing

| Type           | Channel          | Danger Level |
|----------------|------------------|--------------|
| Phishing       | Email (mass)     | High         |
| Spear Phishing | Email (targeted) | Very High    |
| Smishing       | SMS              | High         |
| Vishing        | Voice call       | High         |

### Psychological Triggers Exploited by Attackers

| Trigger     | Example                                        |
|-------------|------------------------------------------------|
| **Urgency** | "Your account will be deleted in 24 hours"     |
| **Fear**    | "Suspicious activity detected on your account" |
| **Greed**   | "You've been selected for a $500 gift card"    |

### Key Red Flags

- Suspicious sender domain (paypa1.com vs paypal.com)
- Mismatched or shortened URLs
- Urgent or threatening language
- Unexpected attachments (.exe, .zip, .docm)
- Grammar and spelling errors
- Requests for credentials via email

---

## 🚀 Usage

No installation needed — just open the file:

```bash
# Simply double-click the file, or:
start phishing_awareness.html
```

Works in any modern browser (Chrome, Firefox, Edge).

---

## 📊 Quiz Results Interpretation

| Score | Level         | Message                                    |
|-------|---------------|--------------------------------------------|
| 5/5   | 🟢 Expert     | Perfect score — share your knowledge!      |
| 4/5   | 🟢 Great      | Solid foundation — review missed questions |
| 3/5   | 🟡 Good       | Review the slides and retry                |
| < 3/5 | 🔴 Needs work | Study the material carefully               |

---

## 🗂️ File Structure

```
Task2_PhishingAwareness/
├── phishing_awareness.html
├── phishing_quiz.html
└── README.md
```

---

## 📚 References

- OWASP Social Engineering: https://owasp.org/www-community/attacks/Social_Engineering
- Anti-Phishing Working Group: https://apwg.org
- NIST Phishing Guidance: https://csrc.nist.gov
