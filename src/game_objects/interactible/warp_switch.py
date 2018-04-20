import pygame

from src.const import *
from src.game_objects.interactible.consumable import Consumable


class WarpSwitch(Consumable):
    width = 50
    height = 50
    color = RED

    def __init__(self, *args,
                 pos, ground,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((WarpSwitch.width, WarpSwitch.height)),
                         is_solid=False,
                         **kwargs)
        self.color = self.__class__.color
        self.image.fill(self.color)
        self.ground = ground
        self.ground.color = self.color
        if self.ground.world is None:
            self.ground.world = "one"
        self.max_timer = 50
        self.timer = self.max_timer

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        if self.timer == 0:
            self.ground.world = "one" if self.ground.world == "two" else "two"
            self.kill()
        else:
            self.timer -= 1
