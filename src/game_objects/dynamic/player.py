import logging

import pygame
from pygame.locals import *

from src.const import *
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.dynamic import Dynamic
from src.game_objects.dynamic.enemy import Enemy
from src.game_objects.effects.warping_effect import WarpingEffect
from src.game_objects.interactible.consumable import Consumable
from src.game_objects.terrain.kill_field import KillField
from src.level.main_menu import MainMenu


class Player(Dynamic):
    
    images = {"run": load_image_folder("../gfx/player/run"),
              "idle": load_image_folder("../gfx/player/idle"),
              "fall": load_image_folder("../gfx/player/fall"),
              "jump": load_image_folder("../gfx/player/jump"),
              "dead_flying": load_image_folder("../gfx/player/dead_flying"),
              "dead_lying": load_image_folder("../gfx/player/dead_lying")}
    
    def __init__(self, *args,
                 warp_charges=99, **kwargs):
        
        super().__init__(*args,
                         image=pygame.Surface((46, 68)),
                         **kwargs)
        self.speed = 6
        self.is_player = True
        self.x_dir = 1
        self.jump_power = 15
        
        self.warp_charges = warp_charges
        self.won = False
        
        self.hp = 1
        self.dying = False
        self.die_counter = 0
        self.stunned = False
        
        self.set_image("idle")
        self.ticks_per_frame = 5
        
        self.won = False

    def update(self):
        super().update()

        ##############
        # physics
        ##############
        self.apply_gravity()
        
        if self.on_ground():
            self.dx = 0
            self.stunned = False
        else:
            self.dx += -sign(self.dx) * .25

        if not self.game.paused and self.is_alive():
            self.process_input()
        
        ##############
        # COLLISION
        ##############
        from src.game_objects.dynamic.chaser import Chaser
        if self.is_alive():
            if self.contact_with(Enemy, "left") or self.contact_with(Enemy, "top"):
                self.get_stunned("left")
                if self._warpable():
                    self.warp()
                else:
                    self.get_hit(1)
            
            elif self.contact_with(Enemy, "right") or self.contact_with(Enemy, "bottom"):
                self.get_stunned("right")
                if self._warpable():
                    self.warp()
                else:
                    self.get_hit(1)
                    
            crushed_enemy = self.contact_with(DumbEnemy, "bottom")
            if crushed_enemy:
                logging.info(f"{self} crushing {crushed_enemy}")
                crushed_enemy.get_hit(1)
    
            collidee = self.collide_with(Consumable)
            if collidee:
                self.consume(collidee)
        ##############
        # winning
        ##############
        if self.won:
            self.game.build_next_level()

        ##############
        # Sprite
        ##############
        if self.is_alive():
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
        else:
            if self.on_ground():
                self.set_image("dead_lying")
            else:
                self.set_image("dead_flying")

        # Menu script auto script
        if isinstance(self.game.level, MainMenu):
            if self.y > 1000:
                self._warp()
                self.y = 0
                self.dy = 0
        
        if self.hp <= 0 and not self.dying:
            self.die()
            self.dying = True
        
        if self.die_counter > 0:
            self.die_counter -= 1
        else:
            if not self.is_alive():
                self.game.reset_level()
            
    def draw(self):
        super().draw()
        
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
            if keys[pygame.K_w] or keys[pygame.K_x] or keys[pygame.K_UP]:
                self.jump()

    def move(self, direction):
        if direction == "left":
            self.x_dir = -1
            self.dx = -self.speed
        if direction == "right":
            self.x_dir = 1
            self.dx = self.speed
    
    def jump(self):
        if self.on_ground():
            self._jump()
    
    def _jump(self):
        self.dy -= self.jump_power
    
    def warp(self):
        # check if going to warp into solid
        if self._warpable():
            self.warp_charges -= 1
            self._warp()
        else:
            collidee = self.detect_solid(self.rect, same_world=False)
            if self.warp_charges <= 0:
                self.game.camera.no_charge_error()
            elif collidee:
                collidee.flash_color(RED, alpha=155, period=5)
                
            self.game.sfxs.play("error")
    
    def _warp(self):
        # Make warp effect
        effect = WarpingEffect(self.game, pos=(self.x, self.y))
        self.game.add_entity(effect)
        
        target_world = "two" if self.game.world == "one" else "one"
        self.world = target_world
        self.game.change_world()
    
    def _warpable(self):
        # check if going to warp into solid
        collidee = self.detect_solid(self.rect, same_world=False)
        return collidee is None and self.warp_charges > 0
    
    def consume(self, consumable):
        consumable.get_consumed(self)
    
    # talk shit
    def get_hit(self, dmg=0):
        self.hp -= dmg

    def get_stunned(self, direction):
        self.dy = -7
        self.stunned = True
        if direction == "left":
            self.dx = -10
        else:
            self.dx = 10
    
    def die(self):
        self.die_counter = 100
        
        # rorate rect 90 degrees for lying pose
        _surf = pygame.Surface(self.rect.size)
        rotated_surf = pygame.transform.rotate(_surf, 90)
        rotated_rect = rotated_surf.get_rect()
        rotated_rect.center = self.rect.center
        
        self.rect = rotated_rect
    
    def is_alive(self):
        return self.hp > 0
    
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

