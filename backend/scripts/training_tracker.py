"""
Appends a training run record to CSV.
"""
import csv, time, os

def main():
    out = os.path.normpath("D:/whisper-laced/backend/training_runs.csv")
    new = not os.path.exists(out)
    with open(out, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["ts","run_id","status","notes"])
        w.writerow([int(time.time()), os.urandom(4).hex(), "ok", "seed run"])
    print("tracked:", out)

if __name__ == "__main__":
    main()
