from src.const import *
from src.game_objects.effects.effect import Effect


class WarpingEffect(Effect):
    
    images = {"static": load_image_folder("../gfx/effects/warping")}
    
    def __init__(self, *args, **kwargs):
        image = pygame.Surface((100, 100))
        super().__init__(*args, image=image, is_solid=False, depth=1, **kwargs)
        
        self.set_image("static")
        
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
    
    def on_ainmation_end(self):
        super().on_ainmation_end()
        self.kill()
