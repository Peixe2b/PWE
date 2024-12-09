from platform import system
from src import *

PWE_Init()
window = PWE_CreateWindow("Game1", 800, 500)

try:
    while PWE_WindowShouldClose(window):
        events = PWEEventController()
        PWELogger.show_warning("WINDOW UPDATE")

        while(PWE_PollEvents(events)):
            pass

        # PWE_UpdateWindow() -> Update window screen
except:
    PWE_Terminate()

