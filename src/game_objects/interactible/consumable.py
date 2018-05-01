import logging

from src.const import *
from src.game_objects.dynamic.dynamic import Dynamic
from src.game_objects.game_object import GameObject


class Consumable(GameObject):
    width = height = 50
    color = L_BLUE

    def __init__(self, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()

    def get_consumed(self, consumer):
        self.game.sfxs.play("collect_charge")
        logging.info(f"{self} consumed by {consumer}")
