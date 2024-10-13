import src as pwe

pwe.PWE_Init()
window = pwe.PWE_CreateWindow("Game1", 800, 500)

while pwe.PWE_WindowShouldClose(window):
    pwe.PWELogger.show_log("Window Update")

pwe.PWE_Terminate()
