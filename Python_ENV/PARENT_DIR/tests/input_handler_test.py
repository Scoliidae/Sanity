"""
Test suite for __package__.sanitation.input_handler

---

NOTE: input_handler is supposed to ALREADY be sterilized from it's own imports

That said if anything is needed that is not already being accessed through that file
ONLY add it to the imports

Unless absolutely needed, do NOT call sanitation._input_handler unless you know what
you are doing

input_handler is used to sterilize returned available functions, classes, & variables in
static type checkers

Most calls available in _input_handler have been provided simpler implementations for
input_handler
"""

#region Imports
from ..sanitation.input_handler import \
    filtered_input,\
    global_kw_args
print(# Imports called
    f"[PACKAGE]:\tCalled {__package__.rsplit('.',1)[0]}.sanition from test suite for access to the following:",
    "[PACKAGE]:\tinput_handler.filtered_input",
    "[PACKAGE]:\tinput_handler.global_kw_args",
    sep="\n"
    )
#endregion

print(f"[TEST]:\t\t{filtered_input('hi','hi','hello',manual_error_handling='ouch',expected_type=str)= }")
print(f"[TEST]:\t\t{global_kw_args()= }")
