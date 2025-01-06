from ctypes import (
    c_uint8, c_uint32,
    c_bool, c_void_p,
    c_wchar_p, c_char_p
)
from typing import (
    Union, Callable, Any
)
from dataclasses import dataclass 
from PWE._pwe_events import *
from PWE.main import *


@dataclass
class PWEWindow:
    x: PWE_NUMBER
    y: PWE_NUMBER
    width: PWE_NUMBER
    height: PWE_NUMBER
    title: str
    is_fullscreen: Union[PWE_TRUE, PWE_FALSE]
    resizable: Union[PWE_TRUE, PWE_FALSE] = PWE_FALSE
    minimizable: Union[PWE_TRUE, PWE_FALSE] = PWE_FALSE
    closed: Union[PWE_TRUE, PWE_FALSE] = PWE_FALSE
    decorated: Union[PWE_TRUE, PWE_FALSE] = PWE_TRUE
    handle: Any = None

@dataclass
class PWEColor:
    r: c_uint8
    g: c_uint8
    b: c_uint8
    a: c_uint8 = 255

@dataclass
class PWEEvent:
    event_name: c_wchar_p
    event_type: Union[c_void_p, c_wchar_p]
    event_callback: Union[None, Callable]
    event_return: Union[c_void_p, Any]    

@dataclass
class PWERectangle:
    pass

@dataclass
class PWEPoint:
    pass
