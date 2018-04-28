class Level():
    
    def __init__(self, game, *args, name=None):
        self.game = game
        self.name = name if name is not None else self.__class__.__name__
