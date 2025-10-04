import sqlite3, os, sys
p = r"D:\whisper-laced\backend\db.sqlite3"
con = sqlite3.connect(p)
cur = con.cursor()

# Make sure table exists (create minimal if someone nuked it)
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reports'")
if not cur.fetchone():
    cur.execute("""
        CREATE TABLE reports(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ref_id INTEGER,
          topic TEXT,
          reason TEXT,
          status TEXT DEFAULT 'open',
          created_at TEXT DEFAULT (datetime('now'))
        )
    """)

# Ensure columns
def has_col(name):
    cur.execute("PRAGMA table_info(reports)")
    return any(r[1] == name for r in cur.fetchall())

if not has_col("target_type"):
    # Add with default so NOT NULL won’t break old rows
    cur.execute("ALTER TABLE reports ADD COLUMN target_type TEXT NOT NULL DEFAULT 'generic'")
else:
    # Fill blanks and make sure nothing is NULL
    cur.execute("UPDATE reports SET target_type='generic' WHERE target_type IS NULL OR target_type=''")

# Optional: make sure other columns exist
for name, ddl in [
    ("topic","TEXT"),
    ("reason","TEXT"),
    ("ref_id","INTEGER"),
    ("status","TEXT"),
    ("created_at","TEXT")
]:
    if not has_col(name):
        cur.execute(f"ALTER TABLE reports ADD COLUMN {name} {ddl}")

con.commit()
print("OK: reports table patched.")
con.close()
