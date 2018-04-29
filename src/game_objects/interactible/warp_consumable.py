from src.const import *
from src.game_objects.interactible.consumable import Consumable


class WarpCharge(Consumable):
    images = {"static": load_image_folder("../gfx/warp_charge")
              }
    width, height = 26, 32

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((WarpCharge.width, WarpCharge.height)),
                         is_solid=False,
                         **kwargs)
        
        self.set_image("static")

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
        
    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        consumer.warp_charges += 1
        
        self.kill()

