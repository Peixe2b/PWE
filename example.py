from platform import system
from src import *

PWE_Init()
window = PWE_CreateWindow("Game1", 800, 500)

while PWE_WindowShouldClose(window):
    events = PWEEventController()

    PWELogger.show_warning("WINDOW UPDATE")
    # PWE_UpdateWindow(window) -> Update window screen

PWE_Terminate()
