from src.const import *
from src.game_objects.game_object import GameObject


class Sign(GameObject):
    images = {"static": [solid_color(ORANGE)]}
    width, height = BLOCK_DIM
    
    def __init__(self, *args, dim, pos, text,**kwargs):
        image = pygame.Surface((Sign.width * dim[0], Sign.height * dim[1]))
        super().__init__(*args,
                         image=image,
                         pos=pos,
                         is_solid=False,
                         depth=1,
                         **kwargs)
        self.set_image("static")
        
        self.text = text
        self.font = pygame.font.Font('src//font//font.otf', 15)
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
        self.render_text(self.text)
