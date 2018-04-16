import pygame


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, game, *args,
                 pos, depth=0, image, **kwargs):
        super().__init__()
        
        self.game = game
        self.x, self.y = pos
        self.depth = depth
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def update(self):
        pass
    
    def draw(self):
        adjusted = self.game.camera.adjust_rect(self.rect)
        print(self.game.camera.rect.center)
        self.game.surface.blit(self.image, adjusted)