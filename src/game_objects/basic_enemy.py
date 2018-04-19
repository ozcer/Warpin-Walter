import pygame

from src.const import *
from src.game_objects.enemy import Enemy


class BasicEnemy(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)

        self.color = L_PURPLE
        self.image.fill(self.color)
        self.speed = 3
        
        self.dir = "left"
        
    def update(self):
        super().update()
        self.apply_gravity()
        self.move(self.dir)
        
        
        if self.detect_solid()
        
    def draw(self):
        super().draw()
    
    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
