from src.const import *
from src.game_objects.dynamic.enemy import Enemy


class DumbEnemy(Enemy):
    images = {"idle": load_image_folder("../gfx/green_slime/idle"),
              "move": load_image_folder("../gfx/green_slime/move"),
              }
    
    width, height = 56, 28
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         image=pygame.Surface((DumbEnemy.width, DumbEnemy.height)),
                         **kwargs)
        self.ticks_per_frame = 8
        self.set_image("idle")
        
        self.speed = 2
        self.hp = 1
        
        self.dir = "left"
        
    def update(self):
        super().update()
        self.apply_gravity()
        self.move(self.dir)
        
        detect_zone = self.rect.copy()
        if self.dir == "left":
            detect_zone.centerx -= 1
        else:
            detect_zone.centerx += 1
        if self.detect_solid(detect_zone):
            self.dir = "right" if self.dir == "left" else "left"
        
        if self.dx != 0 and self.dy != 0:
            self.set_image("move")
        else:
            self.set_image("idle")
        
    def draw(self):
        super().draw()
    
    def move(self, direction):
        if direction == "left":
            self.x_dir = 1
            self.dx = -self.speed
        if direction == "right":
            self.x_dir = -1
            self.dx = self.speed
