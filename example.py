import src as pwe

pwe.PWE_Init()

window = pwe.PWE_CreateWindow("Game1", 800, 500)
running = True

while running and pwe.PWE_WindowShouldClose(window):
    pass
pwe.PWE_Terminate()
