from ctypes import (
    c_int, c_void_p,
    c_wchar_p, c_char_p,
    POINTER, CDLL, cdll
)
from platform import python_version
from typing import Any, Literal, Union

from PWE.main import *
from PWE.config import PWE_NAME, PWE_VERSION
from PWE._pwe_datatypes import (
    PWELogger, PWEWindow
)
from PWE._pwe_errors import *
from PWE.SDL import *

def cleanup_sdl():
    if not isinstance(sdl_singleton.SDL, str):
        del sdl_singleton.SDL

def read_extension_file():
    # Get path
    # Check all files
    # Check type in all files
    # Return extension file
    pass

def run_second_code():
    # Check existent code
    # Try run code
    # Return PWE_TRUE or PWE_FALSE
    pass

def check_platform():
    if PWE_SYSTEM in (
        PWE_PLATFORM_LINUX, PWE_PLATFORM_DARWIN,
        PWE_PLATFORM_WINDOWS
    ): return PWE_TRUE
    # raise PWEPlatformError
    return PWE_FALSE

def get_info() -> tuple:
    PWELogger.show_log(f"PWE version: {PWE_VERSION}")
    PWELogger.show_log(f"System architecture: {PWE_SYSTEM}")
    PWELogger.show_log(f"PWE name: {PWE_NAME}")
    PWELogger.show_log(f"Python version: {python_version()}")
    return (
        PWE_VERSION, PWE_SYSTEM, 
        PWE_NAME, python_version()
    )

def open_sdl_library(cdll_name) -> Union[None, Any]:
    try:
        cdll.LoadLibrary(cdll_name)
        return CDLL(cdll_name)
    except FileNotFoundError:
        PWELogger.show_error(f"SDL library not found: {cdll_name}", PWEPlatformError)
        return None

def init_or_quit_sdl(state: Union[int, None], sdl: Any) -> None:
    sdl.SDL_Init.restype = c_int
    sdl.SDL_Quit.restype = c_void_p

    if state == PWE_INITIALIZE:
        sdl.SDL_Init(PWE_INIT_VIDEO)
        sdl.SDL_Init(PWE_INIT_AUDIO)
        sdl.SDL_Init(PWE_INIT_EVENTS)
        return None
    sdl.SDL_Quit()

def open_window(window: PWEWindow) -> Union[Any, None]:
    try:
        title_encode = c_char_p(window.title)
        window_instance = sdl_singleton.SDL.SDL_CreateWindow(
            title_encode.value, window.x, window.y, window.width,
            window.height, 0
        )
        return window_instance
    except AttributeError as e:
        PWELogger.show_error(f"AttributeError... / {e}", PWEBasicError)
        return None
    except:
        PWELogger.show_error(f"Failed to create window: {window.title}", PWEPlatformError)
        return None
