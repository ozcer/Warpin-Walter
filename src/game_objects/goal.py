import pygame
from src.const import *
from src.game_objects.game_object import GameObject


class Goal(GameObject):
    width = height = 100
    color = RED

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Goal.width, Goal.height)),
                         **kwargs)

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def collide_logic(self, entity):
        try:
            player = entity.is_player
        except AttributeError:
            return None
        finally:
            if player:
                return "goal"
