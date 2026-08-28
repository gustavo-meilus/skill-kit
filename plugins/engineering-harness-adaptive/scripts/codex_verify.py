#!/usr/bin/env python3
"""Compatibility wrapper. The canonical verifier is engineering_verify.py."""
from __future__ import annotations
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("engineering_verify.py")), run_name="__main__")
