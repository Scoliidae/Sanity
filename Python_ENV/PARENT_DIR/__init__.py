"""Initializes everything within the package"""

print(f"[SYSTEM]:\tInitializing package({__package__})...")
print("[PACKAGE]:\tCalling required imports...")
from sys import argv as _argv

from .sanitation import *
from .tests import *

print("[SYSTEM]:\tSuccessfully initialized the package!")
