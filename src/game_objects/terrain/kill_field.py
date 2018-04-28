from src.const import *
from src.game_objects.game_object import GameObject


class KillField(GameObject):
    width, height = 100, 100
    color = BLUE

    def __init__(self, *args,
                 pos,
                 **kwargs):
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((KillField.width, KillField.height)),
                         **kwargs)
        self.color = self.__class__.color
        self.image.fill(self.color)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
