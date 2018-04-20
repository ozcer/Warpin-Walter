import pygame
from src.const import *
from src.game_objects.interactible.consumable import Consumable


class Goal(Consumable):
    width = 25
    height = 100
    color = RED

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((Goal.width, Goal.height)),
                         is_solid=False,
                         **kwargs)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
    
    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        consumer.won = True
        self.kill()
