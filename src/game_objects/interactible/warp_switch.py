from src.const import *
from src.game_objects.interactible.consumable import Consumable


class WarpSwitch(Consumable):
    width = 50
    height = 50
    color = PALETTE_D_BLUE

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
        for ground in self.ground:
            ground.inactive_color = PALETTE_L_GREY
        self.max_timer = 30
        self.timer = 0
        self.depth = 1

    def update(self):
        super().update()

    def draw(self):
        super().draw()

    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        print(self.depth)
        if self.timer == 0 and self.world == self.game.world:
            for ground in self.ground:
                ground.world = "one" if ground.world == "two" else "two"
            self.timer = self.max_timer
        elif self.timer > 0:
            self.timer -= 1
