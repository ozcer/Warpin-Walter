import pygame


# Parses buttons sent from Pygame and translates them into actions
class EventProcessor:

    def __init__(self, state="game"):
        # State determines which methods depending on game state
        self.state = state

    def process(self, event):
        # TODO: Map main menu/pause to escape instead of quitting the game
        if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
            return {"quit": "game"}
        if self.state == "game":
            return self.process_game(event)
        return {None: None}

    # TODO: allow for secondary button_mapping
    @staticmethod
    def process_game(event):
        if event.type == pygame.KEYDOWN:
            # Character probably doesn't "move" up or down
            if event.key == pygame.K_UP:
                return {"move": "up"}
            if event.key == pygame.K_DOWN:
                return {"move": "down"}
            if event.key == pygame.K_LEFT:
                return {"move": "left"}
            if event.key == pygame.K_RIGHT:
                return {"move": "right"}
            # TODO: Figure out a way to handle longer/shorter jumping by holding jump
            if event.key == pygame.K_Z:
                return {"jump": "start"}
            if event.key == pygame.K_X:
                return {"swap": "player"}




