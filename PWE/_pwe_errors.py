class PWETypeError(TypeError):
    """Type Error"""


class PWEBasicException(Exception):
    """Basic raise exception"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
    
    def __str__(self) -> str:
        return self.message
    

class PWEPlatformError(Exception):
    """Platformer Error"""
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)
    
    def __str__(self) -> str: # change to __repr__
        return self.message

