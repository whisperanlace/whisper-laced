import sqlite3, bcrypt, datetime

DB = r"D:\whisper-laced\backend\db.sqlite3"
con = sqlite3.connect(DB)
cur = con.cursor()

# Ensure columns exist on users
cur.execute("PRAGMA table_info(users)")
cols = {r[1] for r in cur.fetchall()}
changed = False

if "is_active" not in cols:
    cur.execute("ALTER TABLE users ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1")
    changed = True
if "is_verified" not in cols:
    cur.execute("ALTER TABLE users ADD COLUMN is_verified INTEGER NOT NULL DEFAULT 0")
    changed = True

# Seed founder user if missing
email = "founder@example.com"
cur.execute("SELECT id FROM users WHERE email=?", (email,))
row = cur.fetchone()
if not row:
    hpw = bcrypt.hashpw(b"ChangeMe123!", bcrypt.gensalt()).decode()
    now = datetime.datetime.utcnow().isoformat()
    cur.execute(
        "INSERT INTO users (email, hashed_password, is_active, is_verified, created_at) VALUES (?, ?, 1, 0, ?)",
        (email, hpw, now)
    )
    changed = True

con.commit()
# Print a minimal summary for PowerShell
cur.execute("PRAGMA table_info(users)")
cols = [r[1] for r in cur.fetchall()]
print("OK users columns:", ",".join(cols))
cur.execute("SELECT id,email,is_active,is_verified FROM users ORDER BY id")
print("OK users rows:", cur.fetchall())
con.close()
