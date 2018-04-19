import pygame

from src.const import *
from src.game_objects.enemy import Enemy
from src.game_objects.player import Player


class Follower(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)
        
        self.color = D_PURPLE
        self.image.fill(self.color)
        self.speed = 3
        
        self.seek_range = 200
        
        
    def update(self):
        super().update()
        self.apply_gravity()
        
        self.seek()
        
    def draw(self):
        super().draw()
    
    def seek(self):
        target = self.find_closest(Player)
        # If found target and within 200 units
        if target is not None and distance((target.x, target.y), (self.x, self.y)) < self.seek_range:
            # Target on left
            if target.x < self.x:
                self.move("left")
            else:
                self.move("right")

    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
