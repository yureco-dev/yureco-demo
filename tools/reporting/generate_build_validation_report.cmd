@echo off
py -3 tools/reporting/generate_build_validation_report.py
IF %ERRORLEVEL% NEQ 0 (
  echo BUILD_VALIDATION_REPORT_FAIL
  exit /b 1
)
echo BUILD_VALIDATION_REPORT_PASS
exit /b 0
