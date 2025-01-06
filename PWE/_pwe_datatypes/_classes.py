from typing import Union, Any
from logging import error, warning, info

from PWE._pwe_events import PWE_EVENTS
from PWE._pwe_errors import PWEBasicError, PWEPlatformError, PWETypeError


class PWELogger(object):
    @staticmethod
    def show_error(
            msg: str,
            error_type: Union[PWEBasicError, PWETypeError, PWEPlatformError]
        ) -> None:
        error(f"{error_type.__name__}... {msg}")
    
    @staticmethod
    def show_log(msg: str) -> None:
        info(msg)
    
    @staticmethod
    def show_warning(msg: str) -> None:
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
