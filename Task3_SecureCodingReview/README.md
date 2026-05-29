# 🔐 Task 3 — Secure Coding Review

![Python](https://img.shields.io/badge/Language-Python%2FFlask-blue?style=flat-square)
![OWASP](https://img.shields.io/badge/Framework-OWASP%20Top%2010-red?style=flat-square)
![Findings](https://img.shields.io/badge/Findings-5%20Vulnerabilities-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

A professional security audit of a Python/Flask application identifying 5 critical vulnerabilities across 3 code modules. Each finding includes vulnerable code, proof of concept, fixed code, and remediation guidance — documented in a formal audit report.

---

## 📋 Findings Summary

| ID      | Vulnerability              | Severity     | OWASP Category         | Status     |
|---------|----------------------------|--------------|----------------------- |------------|
| #001  | SQL Injection              | 🔴 CRITICAL | A01 — Injection        | Remediated |
| #002a | Plaintext Password Storage | 🔴 CRITICAL | A02 — Broken Auth      | Remediated |
| #002b | Sensitive Data in Logs     | 🟠 HIGH     | A03 — Data Exposure    | Remediated |
| #003a | Reflected XSS              | 🟠 HIGH     | A03 — XSS              | Remediated |
| #003b | Debug Mode in Production   | 🔴 CRITICAL | A05 — Misconfiguration | Remediated |

---

## 🧠 Vulnerabilities Explained

### Finding #001 — SQL Injection (CRITICAL)

**Vulnerable code:**
```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)
```

**Attack:** Entering `' OR '1'='1` returns all users from the database.

**Fix — Parameterized queries:**
```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

---

### Finding #002a — Plaintext Password Storage (CRITICAL)

**Vulnerable code:**
```python
if stored_password == password:  # plaintext comparison
    return True
```

**Fix — bcrypt hashing:**
```python
if bcrypt.checkpw(password.encode(), stored_hash):
    return True
```

> bcrypt is intentionally slow (~100 hashes/sec vs 10B/sec for SHA-256), making brute-force attacks impractical.

---

### Finding #002b — Sensitive Data in Logs (HIGH)

**Vulnerable code:**
```python
print(f"Login attempt: username={username}, password={password}")
```

**Fix — Never log credentials:**
```python
logging.info(f"Login success: username={username}")  # password removed
```

---

### Finding #003a — Reflected XSS (HIGH)

**Vulnerable code:**
```python
return f"<h2>Search results for: {query}</h2>"  # unescaped input
```

**Attack:** `/search?q=<script>alert('XSS')</script>` executes JavaScript in the victim's browser.

**Fix — Escape user input:**
```python
safe_query = escape(query)  # converts < > to &lt; &gt;
return f"<h2>Search results for: {safe_query}</h2>"
```

---

### Finding #003b — Debug Mode in Production (CRITICAL)

**Vulnerable code:**
```python
app.run(debug=True)  # exposes Python console — Remote Code Execution risk
```

**Fix:**
```python
app.run(debug=False)
# Or better: app.run(debug=os.getenv('DEBUG', False))
```

---

## 🛠️ Static Analysis Tool

Run **Bandit** to automatically detect Python security issues:

```bash
pip install bandit
bandit -r ./your_project/
```

---

## 🗂️ File Structure

```
Task3_SecureCodingReview/
├── Secure_Code_Audit_Report.docx    # Full professional audit report
└── README.md
```

---

## 📚 References

- OWASP Top 10 2021: https://owasp.org/www-project-top-ten/
- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- Bandit (Python static analyzer): https://bandit.readthedocs.io
- bcrypt: https://pypi.org/project/bcrypt/
- Flask Security: https://flask.palletsprojects.com/en/3.0.x/security/
