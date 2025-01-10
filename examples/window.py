from time import sleep
from PWE import *

PWE_Init()
window = PWE_CreateWindow("MyGame", 800, 500)

if window is None:
    raise OSError()

surface = PWE_GetSurface(window)
PWE_UpdateWindow(window)

sleep(2) # Delay

PWE_Terminate()
