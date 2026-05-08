@echo off
py -3 tools/validators/validate_self_referential_metadata.py
IF %ERRORLEVEL% NEQ 0 (
  echo SELF_REFERENTIAL_METADATA_GATE_FAIL
  exit /b 1
)

py -3 tools/validators/validate_schema_jsonld_url_presence.py
IF %ERRORLEVEL% NEQ 0 (
  echo SCHEMA_JSONLD_URL_GATE_FAIL
  exit /b 1
)

py -3 tools/validators/validate_placeholder_detection.py
IF %ERRORLEVEL% NEQ 0 (
  echo PLACEHOLDER_DETECTION_GATE_FAIL
  exit /b 1
)

py -3 tools/validators/validate_mojibake_detection.py
IF %ERRORLEVEL% NEQ 0 (
  echo MOJIBAKE_DETECTION_GATE_FAIL
  exit /b 1
)

py -3 tools/validators/validate_cta_mismatch_detection.py
IF %ERRORLEVEL% NEQ 0 (
  echo CTA_MISMATCH_DETECTION_GATE_FAIL
  exit /b 1
)

py -3 tools/validators/validate_redirect_pages_in_sitemap_detection.py
IF %ERRORLEVEL% NEQ 0 (
  echo REDIRECT_SITEMAP_GATE_FAIL
  exit /b 1
)

echo PREPUBLISH_VALIDATION_LAYER_PASS
exit /b 0
