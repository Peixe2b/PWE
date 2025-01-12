from ctypes import (
    Structure, c_uint8
)

from PWE.main import *

class SDL_Version(Structure):
    _fields_ = [
        ("major", c_uint8),
        ("minor", c_uint8),
        ("patch", c_uint8)
    ]


def SDL_Init(flags: int) -> bool:
    return PWE_TRUE


def SDL_Quit() -> None:
    pass
