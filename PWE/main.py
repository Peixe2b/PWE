from platform import system
from typing import TypeAlias, Union
from ctypes import c_int


# All system config for initialize
sdl = None
PWE_SYSTEM = system()
PWE_PLATFORM_LINUX: str = "Linux"
PWE_PLATFORM_DARWIN: str = "Darwin"
PWE_PLATFORM_WINDOWS: str = "Windows"
PWE_WINDOW_SDL = "SDL2.dll"
PWE_DARWIN_SDL = "libSDL2.dylib"
PWE_LINUX_SDL = "libSDL2.so" 

# Generate alias type vars
PWE_TRUE = 1
PWE_FALSE = 0
PWE_NUMBER: TypeAlias = Union[c_int, int]
PWE_FPS = 60

# Generate alias type FLAGS
PWE_INITIALIZE: TypeAlias = int 
PWE_QUIT: TypeAlias = int
PWE_INIT_VIDEO = 0x00000020
PWE_INIT_AUDIO = 0x00000010
PWE_INIT_EVENTS = 0x00004000

# PWE Pointers for classes

# PWE Singletons

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
