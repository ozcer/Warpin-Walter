import math
import os
import pygame
import logging

# Display
FPS = 60
CAPTION = "Project Hijack"
DISPLAY_WIDTH = int(640 * 1.2)
DISPLAY_HEIGHT = int(480 * 1.2)
START_WINDOW_POS = (100, 100)

# logging
LOG_LEVEL = 30
EXIT_MESSAGE = "WARNING"

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_GREY = (70, 70, 70)
L_GREY = (100, 100, 100)
RED = (255, 0, 0)
ORANGE = (244, 179, 66)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

PURPLE = (106, 27, 154)
L_PURPLE = (156, 77, 204)
D_PURPLE = (56, 0, 107)

OLIVE = (130, 119, 23)
D_OLIVE = (82, 76, 0)
MAROON = (180, 66, 70)

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
ALL_SPRITES = "ALL"


GRAVITY = .5

def build_row(cls, game, start_pos, next_pos, amount, worlds):
    """
    given start position and next relative position
    build that many items and put them in given worlds
    :param cls: class to build
    :param start_pos: (int, int)
    :param next_pos: (int, int)
    :param amount: int
    :param worlds: [str, str...]
    :return: None
    """
    for i in range(amount):
        for world in worlds:
            instance = cls(game, pos=(start_pos[0] + i * next_pos[0],
                                      start_pos[1] + i * next_pos[1]))
            game.add_entity(instance, world)

def find_closest(self, cls):
    """
    return the the closest instance of a class or None if not found
    :param cls: Type (a class)
    :return: Sprite or None
    """
    closest = None
    shortest_dist = None
    for sprite in self.game.entities[ALL_SPRITES]:
        if isinstance(sprite, cls):
            curr_dist = distance((self.x, self.y), (sprite.x, sprite.y))
            if shortest_dist is None or curr_dist < shortest_dist:
                closest = sprite
                shortest_dist = curr_dist
    return closest


def load_image_folder(path):
    cwd = os.path.dirname(__file__)
    relative_path = os.path.join(cwd, path)
    res = []
    for file in os.listdir(relative_path):
        _path = os.path.join(relative_path, file)
        res.append(pygame.image.load(_path))
    return res

def distance(p1, p2):
    """
    get distance between two points
    """
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def angle(p1, p2):
    """
    get angle between two points
    """
    x_dist = p2[0] - p1[0]
    y_dist = p2[1] - p1[1]
    return math.atan2(-y_dist, x_dist) % (2 * math.pi)


def sign(n):
    """
    get the sign of a number
    """
    return (n > 0) - (n < 0)
