from platform import architecture
from src.pwe import (
    PWE_PLATFORM_LINUX, PWE_PLATFORM_MACOS, PWE_PLATFORM_WINDOW,
    PWE_VERSION, PWELogger, PWEPlatformError
)

PWE_ARCHITECTURE = architecture()

def check_system():
    if PWE_ARCHITECTURE[1] in (
        PWE_PLATFORM_LINUX, PWE_PLATFORM_MACOS, PWE_PLATFORM_WINDOW
    ): return True
    return False

if check_system(): PWELogger.show_log("Ok!")
else: PWELogger.show_error("Erro", PWEPlatformError)
