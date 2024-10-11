#!/usr/bin/python
from typing import (
    Any,
    Union, 
    Optional,
    TypeAlias
)
from ctypes import (
    c_int8, 
    c_int, 
    c_uint8,
    c_uint16,
    c_bool,
    c_char,
    CDLL,
    CFUNCTYPE
)
from dataclasses import dataclass
from logging import info, warning, error
from src.pwe_platform import PWE_ARCHITECTURE, check_system, get_info
from src.pwe_errors import PWEBasicException, PWETypeError, PWEPlatformError

PWE_VERSION: tuple = (1, 0, 0)
PWE_NAME: str = "Python Window Engine"

# ------ PWE type variables ------ #
PWE_TRUE: TypeAlias = c_bool
PWE_FALSE: TypeAlias = c_bool
PWE_NUMBER: TypeAlias = c_int

PWE_LINUX_X11: str = "x11"
PWE_LINUX_WAYLAND: str = "wayland"


class PWELogger(object):
    @staticmethod
    def show_error(
            msg: str,
            error_type: Union[PWEBasicException, PWETypeError, PWEPlatformError]
        ) -> None:
        """_summary_

        Args:
            msg (str): _description_
            error_type (Union[PWEBasicException, PWETypeError, PWEPlatformError]): _description_
        """
        error(f"{error_type.__name__}... {msg}")
    
    @staticmethod
    def show_log(msg: str) -> None:
        """_summary_

        Args:
            msg (str): _description_
        """
        info(msg)
    
    @staticmethod
    def show_warning(msg: str) -> None:
        """_summary_

        Args:
            msg (str): _description_
        """
        warning(msg)


@dataclass
class PWEWindow():
    """
    """
    x: PWE_NUMBER
    y: PWE_NUMBER
    width: PWE_NUMBER
    height: PWE_NUMBER
    title: str
    is_fullscreen: Union[PWE_TRUE, PWE_FALSE]
    resizable: Union[PWE_TRUE, PWE_FALSE] = PWE_FALSE
    minimizable: Union[PWE_TRUE, PWE_FALSE] = PWE_FALSE
    closeable: Union[PWE_TRUE, PWE_FALSE] = PWE_TRUE
    decorated: Union[PWE_TRUE, PWE_FALSE] = PWE_TRUE


def PWE_Init() -> None:
    """_summary_

    Raises:
        PWEPlatformError: _description_
    """
    system_is_valid: Union[PWE_TRUE, PWE_FALSE] = check_system()
    pwe_video_drive: Optional[Union[None, PWE_LINUX_X11, PWE_LINUX_WAYLAND]] = None # type: ignore

    if system_is_valid == PWE_TRUE:
        system_info = get_info()
    else:
        PWELogger.show_error("System is invalid", PWEPlatformError.__name__)
        raise PWEPlatformError("ERROR, Your system not work with PWE")


def PWE_Terminate() -> None:
    pass
