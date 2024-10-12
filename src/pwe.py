from typing import (
    Any,
    Union, 
    TypeAlias,
    List,
    Callable
)
from ctypes import (
    c_int, 
    c_uint8,
    c_uint32,
    c_bool,
    c_wchar_p,
    CDLL,
    CFUNCTYPE
)
from platform import system, python_version
from dataclasses import dataclass
from logging import info, warning, error
from src.pwe_errors import PWEBasicException, PWETypeError, PWEPlatformError

PWE_VERSION: tuple = (1, 0, 0)
PWE_NAME: str = "Python Window Engine"

PWE_INITIALIZE: TypeAlias = int
PWE_QUIT: TypeAlias = int
PWE_TRUE: TypeAlias = c_bool 
PWE_FALSE: TypeAlias = c_bool
PWE_NUMBER: TypeAlias = c_int

PWE_SYSTEM = system()
PWE_PLATFORM_LINUX: str = "Linux"
PWE_PLATFORM_DARWIN: str = "Darwin"
PWE_PLATFORM_WINDOWS: str = "Windows"
PWE_WINDOW_SDL = "SDL2.dll"
PWE_DARWIN_SDL = "libSDL2.dylib"
PWE_LINUX_SDL = "libSDL2.so"


@dataclass
class PWEWindow():
    """_summary_

    Attributes:
        window_handle (int): _description_
        platform (str): _description_
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

@dataclass
class Color:
    r: c_uint8
    g: c_uint8
    b: c_uint8
    a: c_uint8 = 255

@dataclass
class PWEEvent:
    event_name: c_wchar_p
    event_type: Union[c_wchar_p, c_uint32]
    event_callback: Union[c_wchar_p, c_uint32]
    event_return: Union[None, c_uint32]    


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
    def __init__(self, events: List[PWEEvent]):
        self.index = 0

    def next(self) -> Union[None, Any]:
        pass

    def has_more(self) -> bool:
        return True


def check_platform():
    if PWE_SYSTEM in (
        PWE_PLATFORM_LINUX, PWE_PLATFORM_DARWIN,
        PWE_PLATFORM_WINDOWS
    ): return PWE_TRUE 
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
        return CDLL(cdll_name)
    except FileNotFoundError:
        PWELogger.show_error(f"SDL library not found: {cdll_name}", PWEPlatformError)
        return None


def init_or_quit_sdl(state: Union[PWE_INITIALIZE, PWE_QUIT], sdl: Any) -> None: 
    if state == PWE_INITIALIZE:
        sdl.SDL_Init()
        return None
    sdl.SDL_Quit()


def open_window(window: PWEWindow) -> Union[Any, None]:
    try:
        title_encode = window.title.decode()
        window_instance = sdl.SDL_CreateWindow(
            title_encode, window.x, window.y,
            window.width, window.height, None
        )
        return window_instance
    except:
        PWELogger.show_error(f"Failed to create window: {window.title}", PWEPlatformError)
        return None


def PWE_Init() -> Union[PWE_TRUE, PWE_FALSE]:
    """_summary_

    Raises:
        PWEPlatformError: _description_
    """
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

    Parameters:
        None

    Returns:
        None
    """
    init_or_quit_sdl(PWE_QUIT, sdl)


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

    if width < 0 or height < 0:
        PWELogger.show_error("Window dimensions must be positive", PWETypeError)
        return None

    window = PWEWindow(
        50, 50, width, height,
        title.encode(), PWE_FALSE, PWE_FALSE,
        PWE_FALSE, PWE_FALSE, PWE_FALSE
    ) 
    open_window(window)
    return window


def PWE_DestroyWindow(window: PWEWindow) -> None:
    pass


def PWE_WindowShouldClose() -> None:
    pass
