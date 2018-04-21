import pygame

from src.const import *
from src.game_objects.dynamic.enemy import Enemy
from src.game_objects.dynamic.player import Player


class Follower(Enemy):
    
    images = {"idle": load_image_folder("../gfx/slime/idle"),
              "move": load_image_folder("../gfx/slime/move"),
              }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)
        
        self.color = D_PURPLE
        self.image.fill(self.color)
        self.speed = 4
        
        self.seek_range = 400
        self.ticks_per_frame = 5
        self.set_image("idle")
        
    def update(self):
        super().update()
        self.apply_gravity()
        
        self.seek()
        
        if self.dx != 0 and self.dy != 0:
            self.set_image("move")
        else:
            self.set_image("idle")
        
    def draw(self):
        super().draw()
    
    def seek(self):
        target = find_closest(self, Player)
        # If Player not found or too far or super close
        if (target is None
                or distance((target.x, target.y), (self.x, self.y)) > self.seek_range
                or abs(self.x - target.x) < 2):
            self.dx = 0
        else:
            self.render_text("!!!", pos=(0, -50), color=RED)
            # Target on left
            if target.x < self.x:
                self.move("left")
            else:
                self.move("right")

    def move(self, direction):
        if direction == "left":
            self.x_dir = 1
            self.dx = -self.speed
        if direction == "right":
            self.x_dir = -1
            self.dx = self.speed
