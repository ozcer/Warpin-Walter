import logging
import itertools
import pygame

from src.const import *
import pygame
from pygame.locals import *

from src.game_objects.interactible.consumable import Consumable
from src.game_objects.dynamic.dynamic import Dynamic
from src.game_objects.dynamic.enemy import Enemy


class Player(Dynamic):
    
    images = {"run": load_image_folder("../gfx/player/run"),
              "idle": load_image_folder("../gfx/player/idle"),
              "fall": load_image_folder("../gfx/player/fall"),
              "jump": load_image_folder("../gfx/player/jump")}
    
    def __init__(self, *args,
                 **kwargs):
        
        super().__init__(*args,
                         image=pygame.Surface((46, 68)),
                         **kwargs)
        self.speed = 6
        self.is_player = True
        self.x_dir = 1
        
        self.warp_charges = 99
        self.won = False
        
        self.stunned = False
        self.hp = 100
        
        self.set_image("idle")
        self.ticks_per_frame = 5
        

    def update(self):
        super().update()
        
        if self.on_ground():
            self.dx = 0
            self.stunned = False
        else:
            self.dx += -sign(self.dx) * .2
        self.process_input()
        self.apply_gravity()
        
        collidee = self.collide_with(Consumable)
        if collidee:
            self.consume(collidee)

        if self.contact_with(Enemy, "left") or self.contact_with(Enemy, "right"):
            self.get_hit(10)
        
        if self.on_ground():
            if self.dx == 0:
                self.set_image("idle")
            else:
                self.set_image("run")
        else:
            if self.dy <= 0:
                self.set_image("jump")
            else:
                self.set_image("fall")
        
    def draw(self):
        super().draw()
        # self.render_text(f"{self.warp_charges}")
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
                if key == K_p:
                    self.game.build_next_level()
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
        self.x_dir = -self.x_dir
        self.dx = -self.x_dir * 9
        self.stunned = True
        self.hp -= dmg
    
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

