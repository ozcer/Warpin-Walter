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
        collision_flags = []
        x_collidee = self.detect_solid(x_projection)
        if x_collidee:
            x_collision_flag = x_collidee.collide_logic(self)
            if x_collision_flag is None:
                # if collide from right
                if x_collidee.rect.centerx > self.rect.centerx:
                    x_projection.right = x_collidee.rect.left
                    self.dx = 0
                else:
                    x_projection.left = x_collidee.rect.right
                    self.dx = 0
            else:
                collision_flags.append(x_collision_flag)

        y_collidee = self.detect_solid(y_projection)
        if y_collidee:
            y_collision_flag = y_collidee.collide_logic(self)
            if y_collision_flag is None:
                # if collide from bottom
                if y_collidee.rect.centery > self.rect.centery:
                    y_projection.bottom = y_collidee.rect.top
                    self.dy = 0
                else:
                    y_projection.top = y_collidee.rect.bottom
                    self.dy = 0
            else:
                collision_flags.append(y_collision_flag)

        if "goal" in collision_flags:
            exit_message = "YOU WIN!"
            self.game.exit_game(exit_message, log=True)
            
        self.rect.center = x_projection.centerx, y_projection.centery
        self.x, self.y = self.rect.center
    
    def detect_solid(self, rect, same_world=True):
        """
        given a rect return a colliding solid Sprite or None
        :param rect: Rect
        :param same_world: Bool
        :return: Sprite or None
        """
        if same_world:
            for sprite in self.game.entities["ALL"]:
                if sprite is not self and sprite.rect.colliderect(rect) and sprite.world == self.game.world:
                    return sprite
        else:
            for sprite in self.game.entities["ALL"]:
                if sprite is not self and sprite.rect.colliderect(rect) and sprite.world != self.game.world:
                    return sprite
    
    def apply_gravity(self):
        self.dy += GRAVITY