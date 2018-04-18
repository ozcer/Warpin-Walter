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
            self.image.fill(D_GREY)
        else:
            self.image.fill(self.color)
        self.game.surface.blit(self.image, adjusted)

    def collide_logic(self, entity):
        return None
    
    def collide_with(self, collidee, strict=False):
        """
        check collision with all instances of a class or specific instance
        :param collidee: Type(a class) or Sprite
        :param strict: bool True = type comparision False = isinstance()
                       for class collision checking only
        :return: Sprite or None
        """
        # check with all instance of a class
        if type(collidee) == type:
            pass
        # check for specific instance
        else:
            pass
