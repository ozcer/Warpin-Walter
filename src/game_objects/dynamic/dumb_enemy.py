import pygame

from src.const import *
from src.game_objects.dynamic.enemy import Enemy


class DumbEnemy(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)

        self.color = L_PURPLE
        self.image.fill(self.color)
        self.speed = 2
        
        self.dir = "left"
        
    def update(self):
        super().update()
        self.apply_gravity()
        self.move(self.dir)
        
        detect_zone = self.rect.copy()
        if self.dir == "left":
            detect_zone.centerx -= 1
        else:
            detect_zone.centerx += 1
        if self.detect_solid(detect_zone):
            self.dir = "right" if self.dir == "left" else "left"
        
    def draw(self):
        super().draw()
    
    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
