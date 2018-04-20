from src.game_objects.dynamic.dynamic import Dynamic


class Enemy(Dynamic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def update(self):
        super().update()
        
    def draw(self):
        super().draw()
