"""
Custom functions for handling inputs to sterilize for functions

Please call this without the "_" in the name for the sterile script
"""
#region imports
from typing import Any
from sys import \
    modules, \
    argv as _argv, \
    maxsize as int_infinity
from os.path import \
    sep as path_sep,\
    exists,\
    isfile
from math import \
    ceil,\
    floor,\
    log
#endregion
#region filtered inputs
class _VerifyInput:
    """Handles all logic pertaining to sanitizing inputs"""
    #region filtered input validation
    @staticmethod
    def filtered_input(
        value:Any,
        /,
        outbound_prompt:str,
        expected_type:type,
        expected_inputs:Any):
        """
        # Evaluates the value input against the expected type and input(s)

        ---

        :outbound_prompt: is for if the original value failed the check,
        this enables manual input through the console

        Please note that if converting integer to byte, please ensure int>=1
        """

        match str(expected_type)\
            .removeprefix("<class '")\
            .removesuffix("'>")\
            .lower():
            case "bool":
                if isinstance(value,str):
                    yes=(
                        'yes',
                        'y',
                        'true',
                        't'
                    )
                    # starts with a variation on yes/True else default false
                    value= True if value\
                        .strip()\
                        .lower()\
                        .startswith(yes)\
                            else False
                elif isinstance(value,type(None)):# Default using expected inputs
                    value=False if expected_inputs is False or expected_inputs is None else True
                elif isinstance(value,int):
                    match value:
                        case 0:
                            value=False
                        case 1:
                            value=True
            case "str":
                if str(value).strip().lower() not in expected_inputs:
                    sterile_user_input:expected_type= _VerifyInput.filtered_input(
                        input(outbound_prompt).strip().lower(),
                        outbound_prompt=outbound_prompt,
                        expected_type=expected_type,
                        expected_inputs=expected_inputs
                        )
                    value:str=sterile_user_input
            case "nonetype":
                if isinstance(value,str):
                    altered_value=value.strip().lower()
                    match altered_value:
                        case ""|"none"|"nonetype"|"null"|"empty":
                            value=None
                elif isinstance(value,bytes):
                    if value.strip().replace(b" ",b"")==b"":
                        value=None
                elif isinstance(value,int) and value==0:
                    value=None
                elif value==bytes()\
                    or value==bytearray()\
                    or value==range(0)\
                    or value==list()\
                    or value==tuple()\
                    or value==set()\
                    or value==frozenset()\
                    or value==dict():
                    value=None
            case "int":
                if isinstance(value,str):
                    #region identify numeric within string to handle
                    #region round float logic
                    if value.find(".")==value.rfind(".") and value.find(".")!= -1:
                        value_int, value_decimal=value.rsplit(".",1)

                        if value_int=="" \
                            or value_decimal=="" \
                            or not value_int.isnumeric() \
                            or not value_decimal.isnumeric():

                            value=_VerifyInput.filtered_input(
                                input(outbound_prompt).strip().lower(),
                                outbound_prompt= f"Failed to register manual input!\
                                    \r\nAttempting manual input again...\
                                    \r\n{outbound_prompt}",
                                expected_type=expected_type,
                                expected_inputs=expected_inputs
                            )
                        if value_decimal.startswith(("5","6","7","8","9")):
                            value=ceil(float(value))
                        else:
                            value=floor(float(value))
                    #endregion
                    elif value.isnumeric() is True:
                        value=floor(value)
                    else:
                        value=_VerifyInput.filtered_input(
                            input(outbound_prompt).strip().lower(),
                            outbound_prompt=f"Failed to register manual input!\
                                \r\nAttempting manual input again...\
                                \r\n{outbound_prompt}",
                            expected_type=expected_type,
                            expected_inputs=expected_inputs
                        )
                    #endregion
                if isinstance(value,float):
                    value_int, value_decimal= str(value).rsplit(".",1)
                    value= ceil(value)\
                        if value_decimal.startswith(# 5 or above
                            ("5","6","7","8","9")
                        )\
                        else int(value)

                match str(type(expected_inputs))\
                    .removeprefix("<class '")\
                    .removesuffix("'>"):

                    case "int":
                        if value!=expected_inputs:
                            value=expected_inputs
                    case "range":
                        if value>expected_inputs.stop:
                            value=expected_inputs.stop
                        elif value<expected_inputs.start:
                            value=expected_inputs.start

                        if value not in expected_inputs:
                            value=_VerifyInput.filtered_input(
                                input(outbound_prompt).strip().lower(),
                                outbound_prompt=f"Failed to register manual input within range!\
                                    \r\nAttempting manual input again...\
                                    \r\n{outbound_prompt}",
                                expected_type=expected_type,
                                expected_inputs=expected_inputs
                            )

            case "range":
                #region clean input
                if isinstance(value,str):
                    try:
                        value=float(value)
                    except ValueError as err:
                        input(err)
                #endregion
                #region force within range
                if isinstance(value,int):
                    if value<expected_inputs.start:
                        value=expected_inputs.start
                    elif value>expected_inputs.end:
                        value=expected_inputs.end
                #endregion
            case "bytes":
                print(value)
                if isinstance(value,int):
                    value:bytes=value.to_bytes(
                        length=_VerifyInput.use_bnint_get_len_bn4bytes(
                            value,
                            original_base=10,
                            new_base=2
                            ),
                        byteorder="little"
                        ).strip(b"\x00")
                elif isinstance(value,str):
                    value=value.encode('unicode')

                    input("PAUSE SCRIPT, THIS IS FOR DEBUGGING!")
                print(value,type(value))


            case _:
                print(value,type(value), type(expected_inputs), expected_type)

        #region Last attempt to get a working value
        if not isinstance(value,expected_type):
            print(value,type(value), type(expected_inputs), expected_type)
            sterile_user_input:expected_type= _VerifyInput.filtered_input(
                input(outbound_prompt).strip().lower(),
                outbound_prompt=f"\
                    \rFailed to recognize manual input response!\
                    \r\nAttemping another manual input request...\
                    \r\n\
                    \r\n{outbound_prompt}",
                expected_type=expected_type,
                expected_inputs=expected_inputs
            )
            value=sterile_user_input
        #endregion
        return value if isinstance(value,expected_type) else ValueError("Failed to verify input")
    @staticmethod
    def use_bnint_get_len_bn4bytes(value:int,original_base:int,new_base:int):
        """
        Provide the value who's base count you wish to change,
        get the approximate length of the new base of same value

        formula= ceil((log(original_base*value)/log(new_base*value)))

        Due to rounding errors after obtaining byte value of the given integer,
        please remember to .strip(b"\\x00")
        """
        #region Sanitize Inputs
        value=_VerifyInput.filtered_input(
            value,
            "What value were you attempting to use? Range()",
            int,
            range(1,int_infinity,1)
            )
        #endregion
        return ceil((log(original_base*value)/log(new_base*value)))
    #endregion filtered input validation

    @staticmethod
    def global_kw_args()->dict:
        """Formats the received runtime inputs to a dictionary"""
        #region Allowed Console inputs
        allowed_cli_cmds:dict={# flag_name:(FLAGS)
            # -- flag requires bool response
            # -  flag requires passed as arg
            "debug":{
                "--DEBUG":bool,
                "-d":bool
                },
            "test":{
                "--Test-Suite":bool,
                "-ts":bool
                }
        }
        #endregion Allowed Console inputs
        kwargs:dict={
            "pkg_flag":True if _argv[0]=="-m" else False,
            "args":list(),
            "kwargs":dict(),
            "ignored":0
            }

        for arg_kwarg in _argv[1:]:

            print(f"{arg_kwarg= }")

            #region sift for kw, arg formats
            keyword:None|str=None
            if arg_kwarg.count("=")==1:# kwarg format
                keyword, argument= arg_kwarg.split("=")
            argument= None if argument.strip()=="" else argument.strip()

            print(f"{keyword= }\n{argument= }")

            arg_kwarg_type="arg" if keyword is None else "kw"

            print(f"{arg_kwarg_type= }")
            #endregion

            print("checking if allowed keyword...")

            #endregion
        return kwargs


#endregion

#region Allowed access (wrappers)
def filtered_input(
        value:Any, /,
        *expected_inputs,
        expected_type:Any,
        manual_error_handling:None|str
        )->Any|ValueError:
    """
    # Evaluates the value input against the expected type and input(s)

    ---

    Please read the docs for further information
    """
    type(expected_inputs)
    return _VerifyInput.filtered_input(value,
        outbound_prompt=manual_error_handling,
        expected_type=expected_type,
        expected_inputs=expected_inputs
    )
def global_kw_args()-> dict:
    """Returns a dictionary about the runtime commmands given"""
    return _VerifyInput.global_kw_args()
#endregion

#region check how script was loaded
#region check if new sterile script needs to be made
if __name__=='__main__':# if ran directly not in a package
    check_path:str=f"{__file__.rsplit(path_sep,1)[0]}{path_sep}input_handler.py"
    sterile_script_template=[
        '"""\n',
        'One-stop shop for all things inputs\n',
        '\n',
        'Handles everything involving inputs from sterilization to cryptography\n',
        '"""\n',
        '\n',
        'from ._input_handler import filtered_input\n',
        ]

    if not exists(check_path) or not isfile(check_path): # check if script exists
        with open(check_path,'w',encoding='utf-8') as new_sterile_script:
            new_sterile_script.writelines(sterile_script_template)
    elif isfile(check_path): # check script is empty
        # create new script from template if first line is empty
        with open(check_path,'w+',encoding='utf-8') as check_sterile_script:
            if check_sterile_script.readline(1)=="":
                check_sterile_script.writelines(sterile_script_template)
        # otherwise use current existing script
    else:# If script exists and is not empty
        raise OSError(1, "Failed to load script! Please load this script from the generated script")
#endregion
#region Check if package was initialized correctly
ERROR:str|None=None
_if_error_print:str="PkgError('Improperly loaded package!')"
try:# to cause problems and throw error to close script if improperly loaded
    if __package__ is None \
        and f"{__package__}.input_handler" not in modules \
        and __name__ not in modules:
        raise OSError(_if_error_print)
except OSError:# if error was successfully thrown record it
    ERROR=_if_error_print
finally:# Confirm an error was made and raise it
    if ERROR is not None:
        raise OSError(ERROR)
#endregion
#endregion
