from src import *

PWE_Init()
window = PWE_CreateWindow("Game1", 800, 500)
renderer = PWE_CreateRenderer(window)
PWE_RenderPresent(renderer)

while PWE_WindowShouldClose(window):
    events = PWEEventController()

    PWELogger.show_warning("WINDOW UPDATE")
    while PWE_PollEvents(events):
        if events.type == PWE_KEY_SPACE:
            PWELogger.show_warning("Space pressed")
        if events.type == PWE_KEY_ESC:
            PWELogger.show_warning("Close window")
            window.closed = True
    PWE_UpdateWindow(window)

PWE_DestroyWindow(window)
PWE_Terminate()
