from src.const import *
from src.game_objects.interactible.consumable import Consumable


class Goal(Consumable):
    images = {"static": [solid_color(RED)]}
    
    width = 25
    height = BLOCK_DIM[1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((Goal.width, Goal.height)),
                         is_solid=False,
                         **kwargs)
        
        self.set_image("static")
        
    def update(self):
        super().update()

    def draw(self):
        super().draw()
    
    def get_consumed(self, consumer):
        super().get_consumed(consumer)
        consumer.won = True
        self.kill()
