from platform import system
from typing import TypeAlias
from ctypes import c_bool, c_int

from PWE.config import pwe_config, PWE_NAME, PWE_VERSION


# All system config for initialize
sdl = None
PWE_SYSTEM = system()
PWE_PLATFORM_LINUX: str = "Linux"
PWE_PLATFORM_DARWIN: str = "Darwin"
PWE_PLATFORM_WINDOWS: str = "Windows"
PWE_WINDOW_SDL = "SDL2.dll"
PWE_DARWIN_SDL = "libSDL2.dylib"
PWE_LINUX_SDL = "libSDL2.so" 

# Generate alias type

# PWE Type aliases (NOTA: TODAS AS VARIÁVEIS VÃO MUDAR PARA UMA LÓGICA BOOLEANA MELHOR)
PWE_INITIALIZE: TypeAlias = int 
PWE_QUIT: TypeAlias = int
PWE_TRUE: TypeAlias = c_bool # 1
PWE_FALSE: TypeAlias = c_bool # 0
PWE_NUMBER: TypeAlias = c_int 

# PWE Initialize constants
PWE_INIT_VIDEO = 0x00000020
PWE_INIT_AUDIO = 0x00000010
PWE_INIT_EVENTS = 0x00004000
PWE_FPS = 60

# PWE Pointers for classes

def main():
    # System config
    # Load Classes
    # Load engine
    # Load Json files
    # Get All singletons
    pass
