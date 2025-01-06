from PWE import *

PWE_Init()
window = PWE_CreateWindow("MyGame", 800, 500)
surface = PWE_GetSurface(window)

try:
    while True:
        PWE_UpdateWindow(window)
except:
    PWE_Terminate()
