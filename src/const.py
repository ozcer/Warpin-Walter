# display
FPS = 60
CAPTION = "Project Hijack"
DISPLAY_WIDTH = 1040
DISPLAY_HEIGHT = 480
START_WINDOW_POS = (100,100)

# logging
LOG_LEVEL = "NOTSET"

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_GREY = (40, 40, 40)
L_GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (244,179, 66)

OLIVE = (130, 119, 23)
D_OLIVE = (82, 76, 0)
L_OLIVE = (180, 166, 71)

BLUE = (25, 118, 210)
L_BLUE = (99, 164, 255)
D_BLUE = (0, 75, 160)

PALETTE_L_GREY = (76, 84, 91)
PALETTE_D_GREEN = (123, 132, 80)
PALETTE_L_BLUE = (167, 219, 216)
PALETTE_D_BLUE = (105, 210, 231)
PALETTE_L_ORANGE = (243, 134, 48)
PALETTE_D_ORANGE = (250, 105, 0)

PLAYER_COLOR = D_OLIVE

# Group of all entities
ALL_ENTITIES = "ALL"
WORLD_1 = "ONE"
WORLD_2 = "TWO"
BOTH_WORLDS = "BOTH"

GRAVITY = .5


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
