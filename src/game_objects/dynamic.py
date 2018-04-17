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
        
        self.collide_with_solid()
        
    def _apply_kinematics(self):
        projection = self.rect.copy()
        
        projection.centerx = self.x + self.dx
        projection.centery = self.y + self.dy
        adjusted = self.game.camera.adjust_rect(projection)
        pygame.draw.rect(self.game.surface, RED, adjusted)

        collidee = self.detect_solid(projection)
        if collidee:
            if projection.bottom > collidee.rect.top:
                projection.bottom = collidee.rect.top
                self.dy = 0
            elif projection.top < collidee.rect.bottom:
                projection.top = collidee.rect.bottom
                self.dy = 0
                
        collidee = self.detect_solid(projection)
        if collidee:
            if projection.right > collidee.rect.left:
                projection.right = collidee.rect.left - 1
                self.dx = 0
            elif projection.left < collidee.rect.right:
                projection.left = collidee.rect.right + 1
                self.dx = 0
            
        self.rect.center = projection.center
        self.x, self.y = self.rect.center
        
        
        
        # # collision correction
        # collidee = self.collide_with_solid()
        # if collidee is not None:
        #     # horizontal collision adjustment
        #     dx = self.dx
        #     self.dx = 0
        #     if self.rect.right > collidee.rect.left:
        #         self.rect.right = collidee.rect.left
        #     elif self.rect.left < collidee.rect.right:
        #         self.rect.left = collidee.rect.right
        #     else:
        #         self.dx = dx
        #
        #     self.x = self.rect.centerx
        #
        # collidee = self.collide_with_solid()
        # if collidee is not None:
        #     dy = self.dy
        #     self.dy = 0
        #     if self.rect.bottom > collidee.rect.top:
        #         self.rect.bottom = collidee.rect.top
        #     elif self.rect.top < collidee.rect.bottom:
        #         self.rect.top = collidee.rect.bottom
        #     else:
        #         self.dy = dy
        #
        #     self.y = self.rect.centery
    
    def detect_solid(self, rect):
        """
        given a rect return a colliding solid Sprite or None
        :param rect: Rect
        :return: Sprite or None
        """
        for sprite in self.game.entities["ALL"]:
            if sprite is not self and sprite.rect.colliderect(rect):
                return sprite
    
    def collide_with_solid(self):
        """
        check if self is colliding with a solid
        :return: Sprite (collidee) or None
        """
        collidee = pygame.sprite.spritecollideany(self,
                                                  self.game.entities["ALL"],
                                                  self._collide_with_solid)
        return collidee
    
    @staticmethod
    def _collide_with_solid(host, other):
        """
        check if host is colliding with a solid
        :param host: Sprite
        :param other: Sprite
        :return: bool
        """
        result = (other is not host
                  and other.is_solid
                  and host.rect.colliderect(other.rect))
        return result
    
    def apply_gravity(self):
        self.dy += GRAVITY