import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class BackgroundBlock(GameObject):
    images = {"dark_steel": load_image_folder("../gfx/enviro/dark_steel_block")}
    
    width, height = 100, 100
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((BackgroundBlock.width, BackgroundBlock.height)),
                         is_solid=False,
                         depth=1,
                         **kwargs)
        
        self.set_image("dark_steel")
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
    
    def draw_inactive(self):
        self.draw_active()