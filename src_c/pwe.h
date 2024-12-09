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
    resizable bool;
    minimizable bool;
    closed bool;
    decorated bool;
    handle char*;
} PWEWindow;

typedef struct {
    r int;
    g int;
    b int;
    alpha int;
} Color;

typedef struct {
    event_name char*;
    event_type int;
} Event;

typedef enum {
} PWE_KeyCode;

typedef enum {
} PWE_MouseCode;
