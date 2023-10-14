"""
One-stop shop for all things inputs

Handles everything involving inputs from sterilization to cryptography
"""

from ._input_handler import \
    filtered_input,\
    global_kw_args

found_callables:dict={# sort by module name
    __name__:{
        "classes":None,
        "functions":["filtered_input"],
        "lambdas":None,
        "generators":None,
        "variables":["found_callables"]
    }
}
print(# console debugging
    "[PACKAGE]:\tChecking for callables...",
    "[MODULE]:\tAvailable Classes:",
    "[MODULE]:\t\t> NONE",
    "[MODULE]:\tAvailable Functions:",
    "[MODULE]:\t\t> filtered_input",
    "[MODULE]:\tAvailable Lambdas:",
    "[MODULE]:\t\t> NONE",
    "[MODULE]:\tAvailable Generators:",
    "[MODULE]:\t\t> NONE",
    "[MODULE]:\tAvailable Variables:",
    "[MODULE]:\t\t> found_callables",
    sep="\n"
    )# end of console debugging
