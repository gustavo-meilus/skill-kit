@echo off
if /I "%~1"=="baseline" py -3 "%~dp0session_baseline.py"
if /I "%~1"=="gate" py -3 "%~dp0stop_gate.py"
