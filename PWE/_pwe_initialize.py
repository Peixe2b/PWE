from typing import TypeAlias
from ctypes import c_bool, c_int


PWE_VERSION: tuple = (1, 0, 0)
PWE_NAME: str = "Python Window Engine" 

PWE_INITIALIZE: TypeAlias = int
PWE_QUIT: TypeAlias = int
PWE_TRUE: TypeAlias = c_bool 
PWE_FALSE: TypeAlias = c_bool
PWE_NUMBER: TypeAlias = c_int 