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
        
        self.seek_range = 300
        
    def update(self):
        super().update()
        self.apply_gravity()
        
        self.seek()
        
    def draw(self):
        super().draw()
    
    def seek(self):
        target = self.find_closest(Player)
        # If Player not found or too far
        if target is None or distance((target.x, target.y), (self.x, self.y)) > self.seek_range:
            self.dx = 0
        else:
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
