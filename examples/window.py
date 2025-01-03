"""
Create a simple window without event system
"""

from PWE import *

PWE_Init()
window = PWE_CreateWindow("MyGame", 800, 500)

while PWE_WindowShouldClose(window):
    PWE_UpdateWindow(window)

PWE_Terminate()
