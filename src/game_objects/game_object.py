import pygame
from src.const import *


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, game, *args,
                 pos, depth=0, image, world=None, is_solid=True, **kwargs):
        
        super().__init__()
        self.game = game
        self.x, self.y = pos
        self.depth = depth
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        self.is_solid = is_solid
        self.world = world
        
        self.inactive_color = L_GREY
        
        self.font = pygame.font.SysFont('Arial', 30)
    
    def update(self):
        pass
    
    def draw(self):
        adjusted = self.game.camera.adjust_rect(self.rect)
        if self.world is not None and self.world != self.game.world:
            self.image.fill(self.inactive_color)
        else:
            self.image.fill(self.color)
        self.game.surface.blit(self.image, adjusted)
    
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
    
    def detect_solid(self, rect, same_world=True):
        """
        given a rect return a colliding solid Sprite or None
        :param rect: Rect
        :return: Sprite or None
        """
        for sprite in self.game.entities["ALL"]:
            if sprite.rect.colliderect(rect) and sprite.is_solid and sprite is not self:
                # If self or collidee in all world, detects
                if self.world is None or sprite.world is None:
                    return sprite
                # if same_world and same world
                elif not same_world or self.world == sprite.world:
                    return sprite
    
    def render_text(self, text, pos=(0, 0), color=BLACK):
        """
        given position relative to self, blit text
        :param text: Str
        :param pos: (int, int) *note this is relative to self
        :param color: (int, int, int) rgb
        :return: None
        """
        textsurface = self.font.render(text, False, color)
        text_rect = textsurface.get_rect()
        
        # Center Text
        centered_text_pos = pos[0]-text_rect.w/2, pos[1]-text_rect.h/2
        
        # Absolute pos from relative to self
        absolute_pos = (self.x + centered_text_pos[0], self.y + centered_text_pos[1])
        
        # Adjust for camera
        camera_adjusted_pos = self.game.camera.adjust_point(absolute_pos)
        self.game.surface.blit(textsurface, camera_adjusted_pos)
    
    def __str__(self):
        return f"{self.__class__.__name__} at {self.x, self.y}"
