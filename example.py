from src import *

PWE_Init()
window = PWE_CreateWindow("Game1", 800, 500)

while PWE_WindowShouldClose(window):
    events = PWEEventController()

    # PWELogger.show_warning("WINDOW UPDATE")
    while PWE_PollEvents(events):
        if events.type == PWE_KEY_SPACE:
            PWELogger.show_warning("Space pressed")
PWE_Terminate()
