import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class Player(GameObject):
    
    def __init__(self, *args,
                 pos,
                 depth=0,
                 **kwargs):
        
        super().__init__(*args,
                         depth=depth,
                         pos=pos,
                         image=pygame.Surface((50,50)),
                         **kwargs)
        self.image.fill(YELLOW)
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
