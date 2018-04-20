import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class Platform(GameObject):
    width, height = 100, 50

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Platform.width, Platform.height)),
                         **kwargs)
        self.color = D_GREY
        self.image.fill(self.color)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
