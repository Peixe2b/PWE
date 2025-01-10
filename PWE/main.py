from platform import system
from typing import Type, Any
from ctypes import c_int


# All system config for initialize
PWE_SYSTEM: str = system()
PWE_PLATFORM_LINUX: str = "Linux"
PWE_PLATFORM_DARWIN: str = "Darwin"
PWE_PLATFORM_WINDOWS: str = "Windows"
PWE_WINDOW_SDL: str = "SDL2.dll"
PWE_DARWIN_SDL: str = "libSDL2.dylib"
PWE_LINUX_SDL: str = "libSDL2.so" 

# Generate alias type vars
PWE_TRUE: bool = True
PWE_FALSE: bool = False
PWE_NUMBER: Type = c_int
PWE_FPS: int = 60

# Generate alias type FLAGS
PWE_INITIALIZE = 0b00000001
PWE_QUIT = 0b00000000
PWE_INIT_VIDEO = 0x00000020
PWE_INIT_AUDIO = 0x00000010
PWE_INIT_EVENTS = 0x00004000

# Singletons classes
class SDLSingleton:
    def __init__(self) -> None: self.__sdl: Any | None = None
    def set_sdl(self, value: Any) -> None: self.__sdl = value
    @property
    def SDL(self): return self.__sdl # <- Return SDL (None | SDL libc)

# PWE Pointers for classes

# PWE Singletons
sdl_singleton = SDLSingleton()

def main():
    # System config
        # -> Open config file
    # Load Classes
        # -> Load pointers
        # -> Load classes
    # Load engine/Classes config
        # -> Config all classes
    # Set software config
        # -> Generate a simple "dir" --help
    # Set all singletons
        # -> Generate basic API
    pass
