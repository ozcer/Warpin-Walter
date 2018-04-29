from src.const import *
from src.game_objects.game_object import GameObject


class Platform(GameObject):
    width, height = 162, 34
    images = {"static": load_image_folder("../gfx/enviro/steel_platform")}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((Platform.width, Platform.height)),
                         **kwargs)
        self.set_image("static")
        
    def update(self):
        super().update()

    def draw(self):
        super().draw()
