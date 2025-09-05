#!/usr/bin/env python3
"""
Project management CLI for administrative tasks.
Usage:
  python manage.py runserver
  python manage.py migrate
  python manage.py seed_admin
"""
import os
import subprocess
import sys

def runserver():
    host = os.getenv("SERVER_HOST","0.0.0.0")
    port = os.getenv("SERVER_PORT","8888")
    workers = os.getenv("WORKERS","4")
    cmd = ["uvicorn","backend.app.main:app","--host",host,"--port",port,"--workers",workers]
    subprocess.run(cmd)

def migrate():
    subprocess.run(["alembic","upgrade","head"])

def seed_admin():
    subprocess.run(["bash","./scripts/seed_admin.sh"])

def main():
    if len(sys.argv) < 2:
        print("Usage: manage.py [runserver|migrate|seed_admin]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "runserver":
        runserver()
    elif cmd == "migrate":
        migrate()
    elif cmd == "seed_admin":
        seed_admin()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
