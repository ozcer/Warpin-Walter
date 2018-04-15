import pygame

from src.const import *
from src.game_objects.dynamics import Dynamic


class Player(Dynamic):
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((50,50)),
                         **kwargs)
        self.image.fill(YELLOW)
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
