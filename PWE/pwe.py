from typing import (
    Any, Union, 
    TypeAlias 
)
from ctypes import (
    c_int, c_uint8, c_uint32,
    c_bool, c_void_p,
    c_wchar_p, c_char_p, POINTER,
    CDLL, cdll
)

PWE_VERSION: tuple = (1, 0, 0)
PWE_NAME: str = "Python Window Engine"

PWE_INITIALIZE: TypeAlias = int
PWE_QUIT: TypeAlias = int
PWE_TRUE: TypeAlias = c_bool 
PWE_FALSE: TypeAlias = c_bool
PWE_NUMBER: TypeAlias = c_int

from platform import system, python_version
from logging import info, warning, error

from PWE._pwe_constants import *
from PWE._pwe_errors import PWEBasicException, PWETypeError, PWEPlatformError
from PWE._pwe_datatypes import *


sdl = 0b1
PWE_SYSTEM = system()
PWE_PLATFORM_LINUX: str = "Linux"
PWE_PLATFORM_DARWIN: str = "Darwin"
PWE_PLATFORM_WINDOWS: str = "Windows"
PWE_WINDOW_SDL = "SDL2.dll"
PWE_DARWIN_SDL = "libSDL2.dylib"
PWE_LINUX_SDL = "libSDL2.so"

class PWELogger(object):
    @staticmethod
    def show_error(
            msg: str,
            error_type: Union[PWEBasicException, PWETypeError, PWEPlatformError]
        ) -> None:
        """
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

class PWEEventController:
    def __init__(self):
        self.index: int = 0
        # self.events = PWE_EVENTS 
        self.type: Any = None

    def next(self) -> Union[None, Any]:
        if self.has_more():
            self.index += 1
            self.type = PWE_EVENTS[self.index - 1]
            return self.type
        return None

    def has_more(self) -> bool:
        if self.index > len(self.events) - 1:
            return False
        return True


def check_platform():
    if PWE_SYSTEM in (
        PWE_PLATFORM_LINUX, PWE_PLATFORM_DARWIN,
        PWE_PLATFORM_WINDOWS
    ): return PWE_TRUE
    # raise PWEPlatformError
    return PWE_FALSE

def get_info() -> tuple:
    """
    Returns:
        tuple: (PWE version, system architecture, PWE name, Python version)
    """
    PWELogger.show_log(f"PWE version: {PWE_VERSION}")
    PWELogger.show_log(f"System architecture: {PWE_SYSTEM}")
    PWELogger.show_log(f"PWE name: {PWE_NAME}")
    PWELogger.show_log(f"Python version: {python_version()}")
    return (
        PWE_VERSION, PWE_SYSTEM, 
        PWE_NAME, python_version()
    )

def open_sdl_library(cdll_name) -> Union[None, Any]:
    """
    Returns:
        Union[None, Any]: SDL library loaded or None if not found
    """
    try:
        cdll.LoadLibrary(cdll_name)
        return CDLL(cdll_name)
    except FileNotFoundError:
        PWELogger.show_error(f"SDL library not found: {cdll_name}", PWEPlatformError)
        return None

def init_or_quit_sdl(state: Union[PWE_INITIALIZE, PWE_QUIT], sdl: Any) -> None:
    if state == PWE_INITIALIZE:
        sdl.SDL_Init(PWE_INIT_VIDEO)
        sdl.SDL_Init(PWE_INIT_AUDIO)
        sdl.SDL_Init(PWE_INIT_EVENTS)
        return None
    sdl.SDL_Quit()

def open_window(window: PWEWindow) -> Union[Any, None]:
    try:
        title_encode = c_char_p(window.title)
        window_instance = sdl.SDL_CreateWindow(
            title_encode.value, window.x, window.y, window.width,
            window.height, 0
        )
        return window_instance
    except AttributeError as e:
        PWELogger.show_error(f"AttributeError... / {e}", PWEBasicException)
        return None
    except:
        PWELogger.show_error(f"Failed to create window: {window.title}", PWEPlatformError)
        return None



def PWE_Init() -> Union[PWE_TRUE, PWE_FALSE]:
    global sdl
    system_is_valid: Union[PWE_TRUE, PWE_FALSE] = check_platform()

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
    """
    Quits the Simple DirectMedia Layer (SDL) library.

    This function is responsible for properly shutting down the SDL library and releasing any resources it has allocated.
    After calling this function, no SDL functions should be called, and the SDL library should not be used.
    """
    init_or_quit_sdl(PWE_QUIT, sdl)
    del sdl


def PWE_CreateWindow(title: str, width: int, height: int) -> Union[PWEWindow, None]:
    """
    Creates a new window with the specified parameters.

    This function initializes a new window using the Simple DirectMedia Layer (SDL) library.
    The window is created with the specified dimensions, title, and window properties.

    Parameters:
        title: str = window title
        width: int = window width
        height: int = window height

    Returns:
        Union[PWEWindow, None]: A PWEWindow object representing the created window, or None if the window creation failed.
    """

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


def PWE_WindowShouldClose(window: PWEWindow) -> Union[PWE_TRUE, PWE_FALSE]:
    """
    Checks if the specified window should be closed.

    This function checks the 'closed' attribute of the given PWEWindow object.
    If the 'closed' attribute is set to PWE_TRUE, the function returns True, indicating that the window should be closed.
    Otherwise, the function returns False, indicating that the window should not be closed.

    Parameters:
        window (PWEWindow): The PWEWindow object to check for closure.

    Returns:
        Union[PWE_TRUE or PWE_FALSE]: PWE_TRUE if the window should be closed, PWE_FALSE otherwise.
    """

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


def PWE_UpdateWindow(window: PWEWindow) -> Union[PWEBasicException, Any]:
    sdl.SDL_UpdateWindowSurface.argtypes = [c_void_p]
    sdl.SDL_UpdateWindowSurface.restype = c_void_p

    try:
        sdl.SDL_UpdateWindowSurface(window.handle)
    except PWEBasicException as e:
        PWELogger.show_error(f"Failed to update window: {window.title}, because {e}", PWEBasicException)
        return PWEBasicException


def PWE_PollEvents(events: PWEEventController) -> bool:
    """
    Polls for events from the event controller.

    This function iterates through the events in the event controller and processes each event.
    It returns True if there are more events to process, and False if the event controller is empty.

    Parameters:
        events (PWEEventController): The event controller containing the events to be processed.

    Returns:
        bool: True if there are more events to process, False if the event controller is empty.
    """
    while events.has_more():
        events.next()
        # PWELogger.show_warning(str(events.type))

    if events.has_more() == False:
        events.index = 0
        return False
    return True
