import pygame

from src.const import *
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
        for event in self.game.events:
            self.process_event(event)

    def draw(self):
        super().draw()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                self.jump()
            elif event.key == pygame.K_x:
                self.swap()
            elif event.key == pygame.K_LEFT:
                self.move("left")
            elif event.key == pygame.K_RIGHT:
                self.move("right")

    def move(self, direction):
        if direction == "left":
            self.dx -= self.speed
        if direction == "right":
            self.dx += self.speed
