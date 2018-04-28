from src.const import *
from src.game_objects.game_object import GameObject


class Sign(GameObject):
    images = {"static": [solid_color(WHITE)]}
    width, height = BLOCK_DIM
    
    def __init__(self, *args, dim, pos, text,**kwargs):
        image = pygame.Surface((Sign.width * dim[0], Sign.height * dim[1]))
        super().__init__(*args,
                         image=image,
                         pos=pos,
                         is_solid=False,
                         depth=1,
                         **kwargs)
        self.text = text
        
        self.set_image("static")
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
