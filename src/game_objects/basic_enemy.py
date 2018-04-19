from src.game_objects.enemy import Enemy


class BasicEnemy(Enemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
