from PWE import *

PWE_Init()

window = PWE_CreateWindow("MyGame", 800, 500)

try:
    while PWE_WindowShouldClose(window):
        events = PWEEventController()        
        PWE_UpdateWindow(window)
except KeyboardInterrupt:
    PWE_Terminate()
