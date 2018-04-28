from src.const import *
from src.game_objects.game_object import GameObject


class Ground(GameObject):
    images = {"static": load_image_folder("../gfx/enviro/steel_block")}
    
    width, height = 75, 75
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((Ground.width, Ground.height)),
                         **kwargs)
        
        self.set_image("static")
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
