import pygame
from src.const import *
from src.game_objects.game_object import GameObject
from src.game_objects.player import Player


class Goal(GameObject):
    width = height = 100
    color = RED

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Goal.width, Goal.height)),
                         is_solid=False,
                         **kwargs)

    def update(self):
        super().update()
        if self.collide_with(Player, world=self.world):
            print("you won")

    def draw(self):
        super().draw()

