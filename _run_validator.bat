@echo off
cd /d "%~dp0"
py -3 tools\validators\validate_self_referential_metadata.py .
echo EXIT:%ERRORLEVEL%
