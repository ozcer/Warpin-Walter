import pygame

from src.const import *
from src.game_objects.consumable import Consumable


class WarpConsumable(Consumable):
    width = height = 50
    color = L_BLUE

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((WarpConsumable.width, WarpConsumable.height)),
                         is_solid=False,
                         **kwargs)
        self.color = self.__class__.color
        self.image.fill(self.color)

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
        
    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        consumer.warp_charges += 1
        
        self.kill()

