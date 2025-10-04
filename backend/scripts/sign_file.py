import sys, os
from backend.security.signer import sign
def main(name: str, exp: int = 600):
    qs = sign(f"/files/{name}", exp)
    base = os.getenv("PUBLIC_BASE", "http://127.0.0.1:8000")
    print(f"{base}/files/{name}?{qs}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.scripts.sign_file <filename> [exp_seconds]", file=sys.stderr); sys.exit(2)
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 600)
