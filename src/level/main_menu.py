from src.level.level import Level


class MainMenu(Level):
    
    def __init__(self, game):
        name = "Main Menu"
        super().__init__(game, name=name)
    
    def build(self):
        from src.game_objects.dynamic.player import Player
        player = Player(self.game, pos=(0, 0), warp_charges=0)
        self.game.add_entity(player, "one")
        self.game.world = "one"
        self.game.camera.follow(player)
        self.game.paused = True
