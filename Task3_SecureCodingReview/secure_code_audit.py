""" FINDING #001 — SQL Injection """

# Vulnerable code
import sqlite3
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

result = get_user(input("Enter username: "))



# sql injection :     ' OR '1'='1      

# SELECT * FROM users WHERE username = 'alice'   ---- become---->  SELECT * FROM users WHERE username = '' OR '1'='1'   




# Fixed code

import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,)) 
    return cursor.fetchone()

result = get_user(input("Enter username: "))



#  Documentation finding #001
'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINDING #001 — SQL Injection
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Severity  : CRITICAL
Category  : OWASP A01 — Injection
Location  : function get_user(), line 6

Description:
  User input is concatenated directly into an SQL query
  without sanitization, allowing arbitrary SQL execution.

Proof of concept:
  Input  : ' OR '1'='1
  Result : Returns all rows from the users table

Remediation:
  Use parameterized queries (prepared statements).
  Never concatenate user input into SQL strings.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''


#------------------------------------------------------------------------------------------------------------------------------------------------


# FINDING #002 — Broken Auth + Data Exposure #


# Vulnerable code 

import sqlite3
import hashlib

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        stored_password = user[2]  
        if stored_password == password: 
            return True
    return False

print(f"[LOG] Login attempt: username={username}, password={password}")





# Fixed code
import sqlite3
import bcrypt
import logging

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()           # Sel aléatoire unique par mot de passe
    return bcrypt.hashpw(password.encode(), salt)

def login(username: str, password: str) -> bool:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        stored_hash = user[2]
      
        if bcrypt.checkpw(password.encode(), stored_hash):
            logging.info(f"Login success: username={username}") 
            return True

    logging.warning(f"Login failed: username={username}") 
    return False


# Documentation finding #002
'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINDING #002 — Broken Auth + Data Exposure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Severity  : CRITICAL
Category  : OWASP A02 + A03

[A] Plaintext password storage
  Passwords stored and compared in plaintext.
  Remediation: Hash with bcrypt before storing.

[B] Sensitive data in logs
  Passwords written to log files in cleartext.
  Remediation: Never log credentials. Log only
  username + success/failure status.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''




#-----------------------------------------------------------------------------------------------------------------------------------

# FINDING #003 — XSS + Security Misconfiguration


# Vulnerable code

from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q")
    
  
    return f"""
    <html>
        <body>
            <h2>Search results for: {query}</h2>
            <p>No results found.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode is on



# Injection:     /search?q=<script>alert('Hacked!')</script>    



# Fixed code
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    
    safe_query = escape(query)
    
    return f"""
    <html>
        <body>
            <h2>Search results for: {safe_query}</h2>
            <p>No results found.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False) 





#Documentation finding #003
'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINDING #003 — XSS + Security Misconfiguration
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Severity  : HIGH / CRITICAL
Category  : OWASP A03 + A05

[A] Reflected XSS
  User input rendered directly in HTML without
  sanitization — arbitrary JS execution possible.
  Remediation: Escape all user input with escape()
  or use a templating engine (Jinja2) with
  auto-escaping enabled.

[B] Debug mode in production
  debug=True exposes an interactive Python console
  on error pages — full Remote Code Execution risk.
  Remediation: Always set debug=False in production.
  Use environment variables: debug=os.getenv('DEBUG')
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''



