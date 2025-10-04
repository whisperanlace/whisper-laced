"""
Seeds a couple of demo rows (idempotent-ish).
"""
import sqlite3, os

def _path():
    url = os.environ.get("DATABASE_URL", "sqlite:///D:/whisper-laced/backend/db.sqlite3")
    if url.startswith("sqlite:///"):
        return os.path.normpath(url[len("sqlite:///"):])
    return os.path.normpath("D:/whisper-laced/backend/db.sqlite3")

def main():
    p = _path()
    con = sqlite3.connect(p); con.row_factory = sqlite3.Row
    cur = con.cursor()
    # editor seed
    cur.execute("INSERT INTO editor_documents(title) VALUES(?)", ("Welcome Doc",))
    doc_id = cur.lastrowid
    cur.execute("INSERT INTO editor_versions(doc_id,version,body) VALUES(?,?,?)", (doc_id,1,"hello world"))
    con.commit()
    print("seed_db: OK -> doc", doc_id)

if __name__ == "__main__":
    main()
