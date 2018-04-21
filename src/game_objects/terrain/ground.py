import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class Ground(GameObject):
    images = {"static": load_image_folder("../gfx/enviro/steel_block"),}
    
    width, height = 100, 100
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Ground.width, Ground.height)),
                         **kwargs)
        
        self.set_image("static")
        
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
