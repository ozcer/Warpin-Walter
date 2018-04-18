import pygame
from src.const import *

from src.const import *


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, game, *args,
                 pos, depth=0, image, is_solid=True, **kwargs):
        super().__init__()
        
        self.game = game
        self.x, self.y = pos
        self.depth = depth
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        self.is_solid = is_solid

    def update(self):
        pass
    
    def draw(self):
        adjusted = self.game.camera.adjust_rect(self.rect)
        if self.world is not None and self.world != self.game.world:
            self.image.fill(L_GREY)
        else:
            self.image.fill(self.color)
        self.game.surface.blit(self.image, adjusted)

    def set_color(self, world):
        current_world = self.game.world
        if world == BOTH_WORLDS:
            self.color = self.colors[world]
        elif world == current_world:
            self.color = self.colors["Active"]
        else:
            self.color = self.colors["Passive"]
        self.world = world
        self.image.fill(self.color)

    def change_color(self, state):
        if self.world == BOTH_WORLDS:
            self.color = self.colors[BOTH_WORLDS]
            return
        self.color = self.colors[state]
        self.image.fill(self.color)
