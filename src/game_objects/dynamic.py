import pygame

from src.const import *
from src.game_objects.game_object import GameObject


class Dynamic(GameObject):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.dx = 0
        self.dy = 0
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        self._apply_kinematics()

    def _apply_kinematics(self):
        x_projection = self.rect.copy()
        y_projection = self.rect.copy()
    
        x_projection.centerx = self.x + self.dx
        y_projection.centery = self.y + self.dy
        x_adjusted = self.game.camera.adjust_rect(x_projection)
        pygame.draw.rect(self.game.surface, RED, x_adjusted)
    
        y_adjusted = self.game.camera.adjust_rect(y_projection)
        pygame.draw.rect(self.game.surface, GREEN, y_adjusted)
    
        x_collidee = self.detect_solid(x_projection)
        if x_collidee:
            # if collide from right
            if x_collidee.rect.centerx > self.rect.centerx:
                x_projection.right = x_collidee.rect.left
                self.dx = 0
            else:
                x_projection.left = x_collidee.rect.right
                self.dx = 0
    
        y_collidee = self.detect_solid(y_projection)
        if y_collidee:
            # if collide from bottom
            if y_collidee.rect.centery > self.rect.centery:
                y_projection.bottom = y_collidee.rect.top
                self.dy = 0
            else:
                y_projection.top = y_collidee.rect.bottom
                self.dy = 0
    
        self.rect.center = x_projection.centerx, y_projection.centery
        self.x, self.y = self.rect.center

    def detect_solid(self, rect, same_world=True):
        """
        given a rect return a colliding solid Sprite or None
        :param rect: Rect
        :return: Sprite or None
        """
        for sprite in self.game.entities["ALL"]:
            if (sprite.rect.colliderect(rect) and
                sprite.world == self.game.world and
                sprite.is_solid and
                    sprite is not self):
                return sprite
    
    def apply_gravity(self):
        self.dy += GRAVITY