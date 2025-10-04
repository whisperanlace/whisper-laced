"""
Ensures minimum tables exist (idempotent).
"""
import os, sqlite3

def _path():
    url = os.environ.get("DATABASE_URL", "sqlite:///D:/whisper-laced/backend/db.sqlite3")
    if url.startswith("sqlite:///"):
        return os.path.normpath(url[len("sqlite:///"):])
    return os.path.normpath("D:/whisper-laced/backend/db.sqlite3")

def _ensure(con):
    cur = con.cursor()
    # reports
    cur.execute("""CREATE TABLE IF NOT EXISTS reports(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      reporter_id INTEGER,
      target_type TEXT NOT NULL,
      target_id INTEGER NOT NULL,
      reason TEXT NOT NULL,
      details TEXT,
      status TEXT NOT NULL DEFAULT 'open',
      moderation_case_id INTEGER,
      created_at TEXT DEFAULT (datetime('now')),
      updated_at TEXT DEFAULT (datetime('now')),
      ref_id INTEGER,
      topic TEXT
    )""")
    # editor
    cur.execute("""CREATE TABLE IF NOT EXISTS editor_documents(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      created_at TEXT DEFAULT (datetime('now'))
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS editor_versions(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      doc_id INTEGER NOT NULL,
      version INTEGER NOT NULL,
      body TEXT NOT NULL,
      created_at TEXT DEFAULT (datetime('now')),
      UNIQUE(doc_id, version)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS enhancement_requests(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      doc_id INTEGER NOT NULL,
      instruction TEXT NOT NULL,
      created_at TEXT DEFAULT (datetime('now'))
    )""")
    con.commit()

def main():
    path = _path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    con = sqlite3.connect(path)
    try:
        _ensure(con)
        print("init_db: OK ->", path)
    finally:
        con.close()

if __name__ == "__main__":
    main()
