from src.const import *
from src.game_objects.interactible.consumable import Consumable


class WarpConsumable(Consumable):
    images = {"static": [solid_color(L_BLUE)]}
    width = height = 50

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((WarpConsumable.width, WarpConsumable.height)),
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

