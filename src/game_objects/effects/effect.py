from src.game_objects.game_object import GameObject


class Effect(GameObject):
    def __init__(self, *args, death_on_end=True, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.death_on_end = death_on_end
    
    def update(self):
        super().update()
        if self._on_last_frame():
            self.on_ainmation_end()
        
    def draw(self):
        super().draw()
    
    def on_ainmation_end(self):
        pass