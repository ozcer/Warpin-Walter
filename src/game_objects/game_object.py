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
        self.world = None
    
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
    
    def collide_with(self, collidee, **conditions):
        """
        check collision with all instances of a class or specific instance
        :param collidee: Type(a class) or Sprite(an instance)
        :param conditions: dict: additional conditions to meet eg. {"rect.w": 100}
        :return: Sprite or None
        """
        
        # Check with all instance of a class
        if type(collidee) == type:
            for sprite in self.game.entities[ALL_SPRITES]:
                # Check if colliding and isinstance()
                if self.rect.colliderect(sprite.rect) and isinstance(sprite, collidee):
                    # Check additional conditions supplied
                    conditions_met = 0
                    for condition in conditions:
                        if getattr(sprite, condition) == conditions[condition]:
                            conditions_met += 1
                    if conditions_met == len(conditions):
                        return sprite
        
        # Check for specific instance
        else:
            # Basic rect check
            if self.rect.colliderect(collidee.rect):
                return collidee
