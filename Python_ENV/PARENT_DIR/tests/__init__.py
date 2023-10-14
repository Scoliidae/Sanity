"""
Test suite for EVERY file outside of the suite for bug testing every file

Please note this suite must be activated in the console with python -m PARENT_DIRECTORY
"""

print("[PACKAGE]:\tcalled test suite for initialization")
from .input_handler_test import *
print("[PACKAGE]:\tCalled input_handler_test from test suite for access to all non-underscored classes and functions")
print("[PACKAGE]:\tFinished initializing test suite")
