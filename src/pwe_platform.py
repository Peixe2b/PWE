from platform import architecture, python_version
from src.pwe import (
    PWE_PLATFORM_LINUX,
    PWE_TRUE, PWE_FALSE,
    PWE_VERSION, PWE_NAME, 
    PWELogger 
)

PWE_ARCHITECTURE = architecture()
PWE_PLATFORM_LINUX: str = "Linux"


def check_system():
    if PWE_ARCHITECTURE[1] in (PWE_PLATFORM_LINUX): return PWE_TRUE
    return PWE_FALSE


def get_info() -> tuple:
    PWELogger.show_log(f"PWE version: {PWE_VERSION}")
    PWELogger.show_log(f"System architecture: {PWE_ARCHITECTURE}")
    PWELogger.show_log(f"PWE name: {PWE_NAME}")
    PWELogger.show_log(f"Python version: {python_version()}")
    return (
        PWE_VERSION, PWE_ARCHITECTURE[1], 
        PWE_NAME, python_version()
    )
