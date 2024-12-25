""" The module provides the following functions:
    PWE_Init: Initializes the PWE library.
    PWE_Terminate: Terminates the PWE library.
    PWE_CreateWindow: Creates a window.
    PWE_UpdateWindow: Updates the window.
    PWE_WindowShouldClose: Checks if the window should be closed.
    PWE_PollEvents: Polls for events.
    PWE_GetSurface: Retrieves the surface of the window.
    And More...

    Note: The PWE library must be installed and linked before using these functions.

    PWE framework version: 1.0.0 is used for create a game using SDL.
    PWE create a connection to SDL using the "PWE_Init" function.

    PWE is free software released under the Apache license. You can use, 
    modify, and distribute this software freely, don't have to ask permission.
"""


from PWE.pwe import (
    PWE_Init, PWE_Terminate,
    PWE_CreateWindow, PWE_UpdateWindow,
    PWE_WindowShouldClose, PWE_PollEvents,
    PWE_GetSurface, PWEEventController
)
from PWE._pwe_constants import *
