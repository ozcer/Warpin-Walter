import pygame

from src.const import *
from src.game_objects.dynamics import Dynamic


class Player(Dynamic):
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((50,50)),
                         **kwargs)
        self.image.fill(YELLOW)
        self.accepted_events = ["move", "jump", "swap"]
    
    def update(self):
        super().update()
        events = filter(self.accepts_event, self.game.events)
        for event in events:
            key = self.get_event_key(event)
            print(key)
            if key == "move":
                self.move(event)
            elif key == "jump":
                pass
            elif key == "swap":
                pass

    def draw(self):
        super().draw()

    def move(self, event):
        direction = event[self.get_event_key(event)]
        if direction == "left":
            self.dx -= 1
        elif direction == "right":
            self.dx += 1

    def accepts_event(self, event):
        key = self.get_event_key(event)
        if key in self.accepted_events:
            return True
        return False

    @staticmethod
    def get_event_key(event):
        key = list(event.keys())[0]
        return key

    @staticmethod
    def get_event_value(event):
        key = self.get_event_key(event)
        value = list(event.keys())[0]
        return value
