"""
Exports assets metadata (stub).
"""
import json, os

def main():
    out = os.path.normpath("D:/whisper-laced/backend/export_assets.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"assets": []}, f)
    print("exported:", out)

if __name__ == "__main__":
    main()
