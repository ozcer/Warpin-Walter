import logging

import pygame

from src.const import *
import pygame
from pygame.locals import *

from src.game_objects.consumable import Consumable
from src.game_objects.dynamic import Dynamic
from src.game_objects.enemy import Enemy

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
        self.x_dir = 1
        
        self.warp_charges = 99
        self.won = False
        
        self.stunned = False
        self.hp = 100
        
    def update(self):
        super().update()
        if self.on_ground():
            self.dx = 0
            self.stunned = False
        self.process_input()
        self.apply_gravity()
        
        collidee = self.collide_with(Consumable)
        if collidee:
            self.consume(collidee)

        collidee = find_closest(self, Enemy)
        if collidee and collidee.world == self.world:
            if self.rect.top > collidee.rect.bottom or self.rect.bottom > collidee.rect.top:
                if collidee.rect.right == self.rect.left or collidee.rect.left == self.rect.right:
                    self.get_hit(10)

    def draw(self):
        super().draw()
        self.render_text(f"{self.warp_charges}")
        self.render_text(f"{self.hp}", pos=(0, -40))
        
        if self.won:
            self.render_text("YOU WON", pos=(0, -50), color=YELLOW)
        
    def process_input(self):
        for event in self.game.events:
            if event.type == KEYDOWN:
                key = event.key
                if key == pygame.K_SPACE:
                    self.warp()
                if key == K_r or key == K_c:
                    self.game.reset_level()

                # TODO super hacky, don't do as I do, do as I say
                import src.game_objects.levels as levels
                if key == K_p:
                    if self.game.level == levels.test_level:
                        self.game.build_level(levels.two_dumbs)
                    else:
                        self.game.build_level(levels.test_level)
        # Checking pressed keys
        keys = pygame.key.get_pressed()
        
        if not self.stunned:
            # Left and right
            if keys[K_RIGHT] or keys[K_d]:
                self.move("right")
            elif keys[K_LEFT] or keys[K_a]:
                self.move("left")
            # Jumping
            if (keys[pygame.K_w] or keys[pygame.K_x] or keys[pygame.K_UP])and self.on_ground():
                self.dy -= 15
    
    def move(self, direction):
        if direction == "left":
            self.x_dir = -1
            self.dx = -self.speed
        if direction == "right":
            self.x_dir = 1
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
    
    # talk shit
    def get_hit(self, dmg=0):
        self.dy = -6
        self.dx = -self.x_dir * 5
        self.x_dir = -self.x_dir
        self.stunned = True
        self.hp -= dmg
        
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

