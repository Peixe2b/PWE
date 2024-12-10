import ctypes

# Carrega a biblioteca SDL
sdl = ctypes.CDLL("libSDL2.so")

# Define constantes
SDL_INIT_VIDEO = 0x00000020
SDL_WINDOWPOS_CENTERED = 0x2FFF0000
SDL_WINDOW_SHOWN = 0x00000004

# Inicializa o SDL
if sdl.SDL_Init(SDL_INIT_VIDEO) != 0:
    error = ctypes.c_char_p(sdl.SDL_GetError()).value.decode("utf-8")
    raise RuntimeError(f"Erro ao inicializar SDL: {error}")

# Cria a janela
sdl.SDL_CreateWindow.argtypes = [
    ctypes.c_char_p,  # título
    ctypes.c_int,     # posição x
    ctypes.c_int,     # posição y
    ctypes.c_int,     # largura
    ctypes.c_int,     # altura
    ctypes.c_uint32   # flags
]
sdl.SDL_CreateWindow.restype = ctypes.c_void_p

window = sdl.SDL_CreateWindow(
    b"Janela SDL com ctypes",  # Título da janela
    SDL_WINDOWPOS_CENTERED,    # Posição X
    SDL_WINDOWPOS_CENTERED,    # Posição Y
    800,                       # Largura
    600,                       # Altura
    SDL_WINDOW_SHOWN           # Flags
)

if not window:
    error = ctypes.c_char_p(sdl.SDL_GetError()).value.decode("utf-8")
    raise RuntimeError(f"Erro ao criar a janela: {error}")

# Loop principal
running = True
event = ctypes.create_string_buffer(56)  # Estrutura SDL_Event tem 56 bytes
while running:
    while sdl.SDL_PollEvent(ctypes.byref(event)):
        event_type = ctypes.c_int.from_buffer(event).value
        if event_type == 0x100:  # SDL_QUIT = 0x100
            running = False

# Limpa e encerra
sdl.SDL_DestroyWindow(window)
sdl.SDL_Quit()
