class PWETypeError(TypeError):
    """Type Error"""

    def __name__(self) -> str:
        return "PWE Type error"


class PWEBasicError(Exception):
    """Basic raise exception"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
    
    def __str__(self) -> str:
        return self.message
    
    def __name__(self) -> str:
        return "PWE Basic exception"


class PWEPlatformError(Exception):
    """Platformer Error"""
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)
    
    def __str__(self) -> str: # change to __repr__
        return self.message

    def __name__(self) -> str:
        return "PWE Platformer error"
