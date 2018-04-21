import logging
import itertools
import pygame

from src.const import *
import pygame
from pygame.locals import *

from src.game_objects.effects.warping_effect import WarpingEffect
from src.game_objects.interactible.consumable import Consumable
from src.game_objects.dynamic.dynamic import Dynamic
from src.game_objects.dynamic.enemy import Enemy
from src.game_objects.terrain.kill_field import KillField


class Player(Dynamic):
    
    images = {"run": load_image_folder("../gfx/player/run"),
              "idle": load_image_folder("../gfx/player/idle"),
              "fall": load_image_folder("../gfx/player/fall"),
              "jump": load_image_folder("../gfx/player/jump")}
    
    def __init__(self, *args,
                 warp_charges=99, **kwargs):
        
        super().__init__(*args,
                         image=pygame.Surface((46, 68)),
                         **kwargs)
        self.speed = 6
        self.is_player = True
        self.x_dir = 1
        
        self.warp_charges = warp_charges
        self.won = False
        
        self.stunned = False
        self.hp = 100
        
        self.set_image("idle")
        self.ticks_per_frame = 5
        
        self.won = False

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

        kill_top = self.contact_with(KillField, "top")
        kill_bot = self.contact_with(KillField, "bottom")
        if kill_top:
            self.hp = 0
        elif kill_bot:
            self.hp = 0

        crushed_enemy = self.contact_with(Enemy, "bottom")
        if self.contact_with(Enemy, "left"):
            if not self.warp():
                self.get_stunned("left")
                self.get_hit(10)
            else:
                self.get_stunned("left")
        elif self.contact_with(Enemy, "right"):
            if not self.warp():
                self.get_stunned("right")
                self.get_hit(10)
            else:
                self.get_stunned("right")
        if crushed_enemy:
            crushed_enemy.get_hit(1)
        
        if self.won:
            self.game.build_next_level()
        
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
        if self.hp <= 0:
            self.game.reset_level()
        
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
            return True
    
    def _warp(self):
        # Make warp effect
        effect = WarpingEffect(self.game, pos=(self.x, self.y))
        self.game.add_entity(effect)
        
        target_world = "two" if self.game.world == "one" else "one"
        self.world = target_world
        self.game.change_world()
        
    def consume(self, consumable):
        consumable.get_consumed(self)
    
    # talk shit
    def get_hit(self, dmg=0):
        self.hp -= dmg

    def get_stunned(self, direction):
        self.dy = -6
        self.stunned = True
        if direction == "left":
            self.dx = -20
        else:
            self.dx = 20

    
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

