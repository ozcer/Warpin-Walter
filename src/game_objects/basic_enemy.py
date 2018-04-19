import pygame

from src.game_objects.enemy import Enemy


class BasicEnemy(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((50, 50)),
                         **kwargs)

        self.color = YELLOW
        self.image.fill(self.color)
        
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
