"""Handles all things configs"""

from typing import Any, \
    Literal

def save(path:str):
    """Saves user config with current edits"""
def load(config_type:Literal["usr"]|Literal["factory"]|Literal["template"],/,path:str)-> dict:
    """
    Loads one of 3 configs using default paths

    ---

    :path: was only made available for config_type="usr", will have no affect on any other values
    """
