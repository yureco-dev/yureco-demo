import subprocess, sys, pathlib

root = r"d:\Сайти\yureco-demo"
out_file = pathlib.Path(root) / "_prepublish_gate_out.txt"

validators = [
    ("tools/validators/validate_self_referential_metadata.py", "SELF_REFERENTIAL_METADATA_GATE"),
    ("tools/validators/validate_schema_jsonld_url_presence.py", "SCHEMA_JSONLD_URL_GATE"),
    ("tools/validators/validate_placeholder_detection.py", "PLACEHOLDER_DETECTION_GATE"),
    ("tools/validators/validate_mojibake_detection.py", "MOJIBAKE_DETECTION_GATE"),
    ("tools/validators/validate_cta_mismatch_detection.py", "CTA_MISMATCH_DETECTION_GATE"),
    ("tools/validators/validate_redirect_pages_in_sitemap_detection.py", "REDIRECT_SITEMAP_GATE"),
]

lines = []
final_exit = 0

for rel_path, gate_name in validators:
    script = str(pathlib.Path(root) / rel_path)
    r = subprocess.run(
        [sys.executable, script, root],
        capture_output=True,
        cwd=root
    )
    stdout = r.stdout.decode("utf-8", errors="replace")
    stderr = r.stderr.decode("utf-8", errors="replace")
    output = stdout + stderr
    lines.append(f"=== {gate_name} (exit={r.returncode}) ===")
    # Show first line (OK or first MISMATCH) + count
    out_lines = [l for l in output.splitlines() if l.strip()]
    issue_markers = (
        "MISMATCH",
        "DETECTED",
        "FAIL",
        "ERROR",
        "REDIRECT_PAGE_PRESENT_IN_SITEMAP",
        "REDIRECT_RULE_SOURCE_PRESENT_IN_SITEMAP",
    )
    mismatch_lines = [l for l in out_lines if any(marker in l for marker in issue_markers)]
    ok_lines = [l for l in out_lines if "OK" in l or "PASS" in l]
    if r.returncode == 0:
        lines.append(f"  PASS: {ok_lines[0] if ok_lines else out_lines[0] if out_lines else '(no output)'}")
    else:
        lines.append(f"  FAIL: {len(mismatch_lines)} mismatch(es)")
        for ml in mismatch_lines[:5]:
            lines.append(f"    {ml}")
        if len(mismatch_lines) > 5:
            lines.append(f"    ... and {len(mismatch_lines)-5} more")
        final_exit = 1

lines.append("")
if final_exit == 0:
    lines.append("PREPUBLISH_VALIDATION_LAYER_PASS")
else:
    lines.append("PREPUBLISH_VALIDATION_LAYER_FAIL")

result_text = "\n".join(lines)
out_file.write_text(result_text, encoding="utf-8")
print(result_text)
sys.exit(final_exit)
