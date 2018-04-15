import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class Ground(GameObject):
    
    width, height = 100, 100
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Ground.width, Ground.height)),
                         **kwargs)
        self.image.fill(L_BLUE)
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
