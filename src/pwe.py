#!/usr/bin/python

from typing import (
    TypeAliasType,
    Any,
    Union,
    Optional,
)
from ctypes import (
    c_int8,
    c_int16,
    c_int, 
    c_uint8,
    c_uint16,
    c_bool,
    c_char,
    CDLL,
    CFUNCTYPE
)
from logging import info, warning, error
from src.pwe_errors import PWEBasicException, PWETypeError, PWEPlatformError

PWE_VERSION = (1, 0, 0)
PWE_NAME = "Python Window Engine"

PWE_PLATFORM_LINUX = "Linux"
PWE_PLATFORM_WINDOW = "Window"
PWE_PLATFORM_MACOS = "Darwin"

# ------ PWE type variables ------ #
PWE_TRUE: TypeAliasType = c_bool
PWE_FALSE: TypeAliasType = c_bool
PWE_NUMBER: TypeAliasType = c_int


class PWELogger(object):
    def __init__(self):
        pass

    @staticmethod
    def show_error(
            msg: str,
            error_type: Union[PWEBasicException, PWETypeError, PWEPlatformError]
        ):
        error(f"{error_type.__name__}... {msg}")
    
    @staticmethod
    def show_log(msg: str):
        info(msg)
    
    @staticmethod
    def show_warning(msg: str):
        warning(msg)
