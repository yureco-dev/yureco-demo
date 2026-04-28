"""Run the CTA mismatch validator for chat and always exit 0."""

from __future__ import annotations

import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent
VALIDATOR = ROOT / "tools" / "validators" / "validate_cta_mismatch_detection.py"
OUT_FILE = ROOT / "_cta_val_out.txt"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ROOT)],
        capture_output=True,
        cwd=ROOT,
    )

    combined = (result.stdout + result.stderr).decode("utf-8", errors="replace")
    OUT_FILE.write_text(combined, encoding="utf-8")

    mismatch_lines = [
        line for line in combined.splitlines() if "CTA_MISMATCH_DETECTED" in line
    ]
    status = "FAIL" if mismatch_lines or result.returncode != 0 else "PASS"

    print(f"CTA_MISMATCH_VALIDATOR_{status}")
    print(f"MISMATCH_COUNT:{len(mismatch_lines)}")
    if mismatch_lines:
        print("\n".join(mismatch_lines[:50]))
        if len(mismatch_lines) > 50:
            print(f"... and {len(mismatch_lines) - 50} more")
    else:
        print(combined[:3000])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
