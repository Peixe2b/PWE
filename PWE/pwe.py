from typing import (
    Any, Union, Literal
)
from ctypes import c_int, c_void_p, c_char_p


from PWE.main import *
from PWE.config import *
from PWE._pwe_datatypes import * 
from PWE._pwe_events import *
from PWE._pwe_errors import PWEBasicError, PWETypeError, PWEPlatformError
from PWE.core.utils import *


def PWE_Init() -> Literal[True, False]: # Initialize SDL 
    global sdl
    system_is_valid: Literal[True, False] = check_platform()

    if system_is_valid != PWE_TRUE:
        PWELogger.show_error("System is invalid", PWEPlatformError)
        return PWE_FALSE
    
    system_info = get_info()
    if system_info[1] == PWE_PLATFORM_LINUX:
        sdl = open_sdl_library(PWE_LINUX_SDL)
    elif system_info[1] == PWE_PLATFORM_DARWIN:
        sdl = open_sdl_library(PWE_DARWIN_SDL)
    elif system_info[1] == PWE_PLATFORM_WINDOWS:
        sdl = open_sdl_library(PWE_WINDOW_SDL)
    init_or_quit_sdl(PWE_INITIALIZE, sdl)
    return PWE_TRUE


def PWE_Terminate() -> None:
    init_or_quit_sdl(PWE_QUIT, sdl)


def PWE_CreateWindow(title: str, width: int, height: int) -> Union[PWEWindow, None]:
    sdl.SDL_CreateWindow.argtypes = [
        c_char_p, c_int, c_int, c_int,
        c_int, c_int
    ]
    sdl.SDL_CreateWindow.restype = c_void_p

    if width < 0 or height < 0:
        PWELogger.show_error("Window dimensions must be positive", PWETypeError)
        return None

    window = PWEWindow(
        50, 50, width, height,
        title.encode(), PWE_FALSE, PWE_FALSE,
        PWE_FALSE, PWE_FALSE, PWE_FALSE
    ) 
    window.handle = open_window(window)
    return window


def PWE_WindowShouldClose(window: PWEWindow) -> Literal[True, False]:
    if window.closed == PWE_TRUE:
        return PWE_TRUE
    return PWE_FALSE


def PWE_GetSurface(window: PWEWindow) -> Any:
    sdl.SDL_GetWindowSurface.argtypes = [c_void_p]
    sdl.SDL_GetWindowSurface.restype = c_void_p

    if window.handle is not None:    
        surface = sdl.SDL_GetWindowSurface(window.handle)
        return surface
    return None


def PWE_UpdateWindow(window: PWEWindow) -> Union[PWEBasicError, Any]:
    sdl.SDL_UpdateWindowSurface.argtypes = [c_void_p]
    sdl.SDL_UpdateWindowSurface.restype = c_void_p

    try:
        sdl.SDL_UpdateWindowSurface(window.handle)
    except PWEBasicError as e:
        PWELogger.show_error(f"Failed to update window: {window.title}, because {e}", PWEBasicError)
        return PWEBasicError


def PWE_PollEvents(events: PWEEventController) -> bool:
    while events.has_more():
        events.next()

    if events.has_more() == False:
        events.index = 0
        return False
    return True
 