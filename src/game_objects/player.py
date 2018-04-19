import logging

import pygame

from src.const import *
import pygame
from pygame.locals import *
from src.game_objects.dynamic import Dynamic
from src.game_objects.ground import Ground
from src.game_objects.warp_consumable import WarpConsumable


class Player(Dynamic):
    
    def __init__(self, *args,
                 **kwargs):
        
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)
        self.color = BLUE
        self.image.fill(self.color)
        self.speed = 7
        self.is_player = True
        
        self.warp_charges = 3
    
    def update(self):
        super().update()
        self.dx = 0
        self.process_input()
        self.game.camera.rect.center = self.x, self.y
        self.apply_gravity()
        
        collidee = self.collide_with(WarpConsumable)
        if collidee:
            self.consume(collidee)

    def draw(self):
        super().draw()
        self.render_text(f"{self.warp_charges}")
        
    def process_input(self):
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    if self.warp():
                        return
                if key == pygame.K_r or key == pygame.K_c:
                    self.game.reset = True
        # Checking pressed keys
        keys = pygame.key.get_pressed()
        
        # Left and right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move("right")
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move("left")
        # Jumping
        if (keys[pygame.K_w] or keys[pygame.K_x] or keys[pygame.K_UP])and self.on_ground():
            self.dy -= 15

    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed

    def warp(self):
        # check if going to warp into solid
        collidee = self.detect_solid(self.rect, same_world=False)
        if collidee is None and self.warp_charges > 0:
            self.warp_charges -= 1
            self._warp()
    
    def _warp(self):
        target_world = "two" if self.game.world == "one" else "one"
        self.world = target_world
        self.game.world = target_world
        
    def consume(self, consumable):
        consumable.get_consumed(self)
    
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

