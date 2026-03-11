from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GUIDE = BASE / "guide"

if not GUIDE.exists():
    print(f"ERROR: folder not found -> {GUIDE}")
    raise SystemExit(1)

files = sorted(GUIDE.glob("*.html"))

print(f"FOUND: {len(files)} html files in /guide")
print("-" * 80)

for f in files:
    print(f.name)