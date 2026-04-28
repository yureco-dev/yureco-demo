#!/usr/bin/env python3
"""
Build validation report generator.

Computes 5 metrics from existing QA artifacts and validator output:

  INDEXABLE_URL_COUNT  — total lines in page_type_inventory.txt
  REDIRECT_PAGE_COUNT  — lines with type "redirect-page" in inventory
  PLACEHOLDER_PAGE_COUNT — count of PLACEHOLDER_DETECTED lines from validator
  META_MISMATCH_COUNT  — lines in self_referential_metadata_mismatch_list.txt
  CTA_MISMATCH_COUNT   — count of CTA_MISMATCH_DETECTED lines from validator

Output (stdout):
  INDEXABLE_URL_COUNT=<value>
  REDIRECT_PAGE_COUNT=<value>
  PLACEHOLDER_PAGE_COUNT=<value>
  META_MISMATCH_COUNT=<value>
  CTA_MISMATCH_COUNT=<value>

Exit code 0 — all metrics computed successfully
Exit code 1 — at least one metric could not be computed

Usage:
    py -3 tools/reporting/generate_build_validation_report.py [REPO_ROOT]
    REPO_ROOT defaults to the current working directory.
"""

import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Metric helpers
# ---------------------------------------------------------------------------

def _count_inventory_lines(inventory_path: Path) -> tuple[int, int] | None:
    """Return (total_lines, redirect_page_count) or None on error."""
    if not inventory_path.exists():
        print(f"ERROR: not found: {inventory_path}", file=sys.stderr)
        return None
    lines = [l.strip() for l in inventory_path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    total = len(lines)
    redirect = sum(
        1 for l in lines
        if len(l.split("|")) >= 2 and l.split("|")[1].strip().lower() == "redirect-page"
    )
    return total, redirect


def _count_mismatch_list(mismatch_path: Path) -> int | None:
    """Return count of non-empty lines in mismatch list, or None on error."""
    if not mismatch_path.exists():
        print(f"ERROR: not found: {mismatch_path}", file=sys.stderr)
        return None
    lines = [l for l in mismatch_path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    return len(lines)


def _run_validator_count(validator_path: Path, marker: str, root: Path) -> int | None:
    """Run a validator script and count stdout lines containing marker."""
    if not validator_path.exists():
        print(f"ERROR: not found: {validator_path}", file=sys.stderr)
        return None
    try:
        result = subprocess.run(
            [sys.executable, str(validator_path), str(root)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        count = sum(1 for line in result.stdout.splitlines() if marker in line)
        return count
    except Exception as e:
        print(f"ERROR running {validator_path}: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    inventory_path = root / "docs" / "qa" / "p2.1" / "page_type_inventory.txt"
    mismatch_path = root / "docs" / "qa" / "p0.3" / "self_referential_metadata_mismatch_list.txt"
    placeholder_validator = root / "tools" / "validators" / "validate_placeholder_detection.py"
    cta_validator = root / "tools" / "validators" / "validate_cta_mismatch_detection.py"

    error = False

    # INDEXABLE_URL_COUNT + REDIRECT_PAGE_COUNT
    inventory_result = _count_inventory_lines(inventory_path)
    if inventory_result is None:
        error = True
        indexable_count = "ERROR"
        redirect_count = "ERROR"
    else:
        indexable_count, redirect_count = inventory_result

    # META_MISMATCH_COUNT
    meta_count = _count_mismatch_list(mismatch_path)
    if meta_count is None:
        error = True
        meta_count = "ERROR"

    # PLACEHOLDER_PAGE_COUNT
    placeholder_count = _run_validator_count(placeholder_validator, "PLACEHOLDER_DETECTED", root)
    if placeholder_count is None:
        error = True
        placeholder_count = "ERROR"

    # CTA_MISMATCH_COUNT
    cta_count = _run_validator_count(cta_validator, "CTA_MISMATCH_DETECTED", root)
    if cta_count is None:
        error = True
        cta_count = "ERROR"

    # Output
    print(f"INDEXABLE_URL_COUNT={indexable_count}")
    print(f"REDIRECT_PAGE_COUNT={redirect_count}")
    print(f"PLACEHOLDER_PAGE_COUNT={placeholder_count}")
    print(f"META_MISMATCH_COUNT={meta_count}")
    print(f"CTA_MISMATCH_COUNT={cta_count}")

    sys.exit(1 if error else 0)


if __name__ == "__main__":
    main()
