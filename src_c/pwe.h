#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PWE_TRUE true
#define PWE_FALSE false
#define PWE_INIT_VIDEO "Initialize video"
#define PWE_INIT_EVENTS "Initialize events"
#define PWE_INIT_TIMER "Initialize timers"

typedef struct {
    x int;
    y int;
    width int;
    height int;
    title char*;
    is_fullscreen bool;
    is_resizable bool;
    is_visible bool;
    is_active bool;
    is_focused bool;
    is_minimized bool;
    is_maximized bool;
    is_decorated bool;
    closeable bool;
    decorated bool;
} PWEWindow;

typedef struct {
    r int;
    g int;
    b int;
    alpha int;
} Color;

typedef enum {
} PWE_KeyCode;

typedef enum {
} PWE_MouseCode;


void PWE_Init(uint *flag);
PWEWindow* PWE_CreateWindow(const char* title, int width, int height, int flag);
void PWE_Terminate(uint *flag);
