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
        self.color = YELLOW
        self.image.fill(self.color)
        self.speed = 7
        self.is_player = True
    
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
        if (keys[pygame.K_w] or keys[pygame.K_SPACE])and self.on_ground():
            self.dy -= 15
        # Warping
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_x:
                    self.warp()
                if key == pygame.K_r or key == pygame.K_c:
                    self.game.reset = True

    def move(self, direction):
        if direction == "left":
            self.dx = -self.speed
        if direction == "right":
            self.dx = self.speed
    
    def warp(self):
        self.game.world = "two" if self.game.world == "one" else "one"
    
    def on_ground(self):
        detector = self.rect.copy()
        detector.bottom += 1
        if self.detect_solid(detector):
            return True
        return False
