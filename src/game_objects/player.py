import pygame

from src.const import *
from pygame.locals import *
from src.game_objects.dynamics import Dynamic


class Player(Dynamic):
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((50, 50)),
                         **kwargs)
        self.color = YELLOW
        self.image.fill(self.color)
        self.speed = 7
    
    def update(self):
        super().update()
        self.dx = 0
        self.process_event()
        self.game.camera.rect.center = self.x, self.y

    def draw(self):
        super().draw()

    def process_event(self):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_RIGHT]:
            self.move("right")
        if keys[pygame.K_LEFT]:
            self.move("left")

    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
