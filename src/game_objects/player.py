import pygame

from src.const import *
import pygame
from pygame.locals import *
from src.game_objects.dynamic import Dynamic


class Player(Dynamic):
    
    def __init__(self, *args,
                 pos,
                 **kwargs):
        
        super().__init__(*args,
                         pos=pos,
                         image=pygame.Surface((50, 50)),
                         **kwargs)

        self.colors = {BOTH_WORLDS: PLAYER_COLOR}
        self.speed = 7
    
    def update(self):
        super().update()
        self.dx = 0
        self.process_event()
        self.game.camera.rect.center = self.x, self.y
        self.apply_gravity()

    def draw(self):
        super().draw()

    def process_event(self):
        # Checking pressed keys
        keys = pygame.key.get_pressed()

        # Left and right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move("right")
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move("left")
        # Jumping
        if (keys[pygame.K_w] or keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_z])and self.on_ground():
            self.dy -= 15
        # Warping
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.warp()

        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_x:
                    self.warp()
                elif key == pygame.K_r or key == pygame.K_c:
                    self.reset()

    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
    
    def warp(self):
        self.game.world = "two" if self.game.world == "one" else "one"
        print(f"world switched to {self.game.world}")
        print(f"player world {self.world}")

    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False

    def warp(self):
        self.game.warp_world()

    def reset(self):
        self.game.reset()
