from src.game_objects.dynamic.dynamic import Dynamic


class Enemy(Dynamic):
    hp = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def update(self):
        super().update()
        
    def draw(self):
        super().draw()

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
