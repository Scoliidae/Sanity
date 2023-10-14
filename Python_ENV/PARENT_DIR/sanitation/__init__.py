"""
# Sanitation

This suite is the custodian of all inputs within the python scripts

---

The primary job is to sterilize and handle volatile variables

This suite is intended to be used in packages so be sure to have this in the root of your package

---

To initialize a package use the following:

```python -m PARENT_DIR```
"""

print("[PACKAGE]:\tcalled sanitation for initialization")
from .input_handler import *
print("[PACKAGE]:\tCalled input_handler from sanitation for access to all non-underscored classes and functions")
print("[PACKAGE]:\tFinished initializing sanitation")
