from PWE import *

PWE_Init()
window = PWE_CreateWindow("Game1", 800, 500)
surface = PWE_GetSurface(window)

try:
    while PWE_WindowShouldClose(window):
        events = PWEEventController()

        while(PWE_PollEvents(events)):
            pass

        PWE_UpdateWindow(window)
except:
    PWE_Terminate()

