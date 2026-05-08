import json
import os
import subprocess
import sys

ROOT = os.getcwd()

VALIDATION_DIR = os.path.join(ROOT, "validation", "self_referential_metadata")

DISCOVER_SCRIPT = os.path.join(VALIDATION_DIR, "discover_metadata_sources.py")
VALIDATOR_SCRIPT = os.path.join(VALIDATION_DIR, "validate_metadata_url_consistency.py")

SOURCE_MAP_FILE = os.path.join(VALIDATION_DIR, "source_map_metadata_urls.json")
MISMATCH_REPORT_FILE = os.path.join(VALIDATION_DIR, "metadata_url_mismatch_report.json")
MASTER_REPORT_FILE = os.path.join(VALIDATION_DIR, "p0_3_master_report.json")


def fail(message):
    report = {"status": "FAIL", "phase": "P0.3", "message": message}
    os.makedirs(VALIDATION_DIR, exist_ok=True)
    with open(MASTER_REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print("P0.3 FAIL")
    sys.exit(1)


def run(script):
    result = subprocess.run([sys.executable, script], cwd=ROOT)
    return result.returncode


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if not os.path.isfile(DISCOVER_SCRIPT):
    fail("discover_metadata_sources.py missing")

if not os.path.isfile(VALIDATOR_SCRIPT):
    fail("validate_metadata_url_consistency.py missing")


if run(DISCOVER_SCRIPT) != 0:
    fail("discover_metadata_sources.py failed")

if not os.path.isfile(SOURCE_MAP_FILE):
    fail("source_map_metadata_urls.json missing")


if run(VALIDATOR_SCRIPT) != 0:
    fail("validate_metadata_url_consistency.py failed")

if not os.path.isfile(MISMATCH_REPORT_FILE):
    fail("metadata_url_mismatch_report.json missing")


report = {
    "status": "PASS",
    "phase": "P0.3",
    "source_map": SOURCE_MAP_FILE,
    "mismatch_report": MISMATCH_REPORT_FILE
}

with open(MASTER_REPORT_FILE, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("P0.3 PASS")
sys.exit(0)
