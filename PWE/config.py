PWE_VERSION: tuple = (1, 0, 0)
PWE_NAME: str = "Python Window Engine" 

LINUX_SDL_PATH = "" # Path for linux
LINUX_OPENGL_PATH = "" # Path for linux

pwe_config = {
    "project": PWE_NAME,
    "version": PWE_VERSION,
    "author": "",
    "description": "",
    "license": "",
    "platforms": ["Linux"],
    "dependencies": ["ctypes", "pytest"],
    "modules": ["PWE"],
    "scripts": [],
    "data_files": [],
    "singleton_files": []
}
