@echo off

py -3 scripts\validate_utf8_mojibake.py

IF %ERRORLEVEL% NEQ 0 (
    echo UTF8 VALIDATION FAILED
    exit /b 1
)

echo UTF8 VALIDATION PASSED
exit /b 0
