import logging
import os
import random
import sys

from src.camera import Camera
from src.event_processor import EventProcessor

import pygame
from pygame.locals import *
from src.const import *
from src.game_objects.ground import Ground
from src.game_objects.player import Player


class Game:
    
    def __init__(self):
        # Pygame window setups
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        logging.basicConfig(level=LOG_LEVEL,
                            datefmt='%m/%d/%Y %I:%M:%S%p',
                            format='%(asctime)s %(message)s')

        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
        self.fps_clock = pygame.time.Clock()
        self.events = pygame.event.get()
        
        screen = pygame.Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.camera = Camera(screen)
        
        player = Player(self, pos=(200, 200))
        self.add_entity(player)

        self.event_processor = EventProcessor()
        
        for i in range(7):
            ground = Ground(self, pos=(i * Ground.width + Ground.width /2 ,
                                       DISPLAY_HEIGHT - Ground.height /3 ))
            self.add_entity(ground)
        
        self.run()
    
    def run(self):
        while True:
            self.surface.fill(L_GREY)
            
            self.update_all_sprites()
            self.draw_all_sprites()

            pygame.display.update()
            self.fps_clock.tick(FPS)

            self.events = map(self.event_processor.process, pygame.event.get())

            for event in self.events:
                quit_game = event.get("quit_game")
                move = event.get("move")
                jump = event.get("jump")
                swap = event.get("swap")

                if quit_game:
                    pygame.quit()
                    sys.exit()

                if move:
                    if move == "left":
                        pass

                    elif move == "right":
                        pass

                if jump:
                    if jump == "start":
                        pass

                if swap:
                    if swap == "player":
                        pass

    def update_all_sprites(self):
        # update all objects
        for sprite in self.entities[ALL_SPRITES]:
            sprite.update()
    
    def draw_all_sprites(self):
        # draw abased on depth
        for sprite in sorted(self.entities[ALL_SPRITES],
                             key=lambda sprite: sprite.depth,
                             reverse=True):
            sprite.draw()
    
    def add_entity(self, entity):
        # add to its own sprite group
        class_name = entity.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(entity)
        logging.info(f"{entity} created")
        
        # also add to global sprite group
        self.entities[ALL_SPRITES].add(entity)
    

if __name__ == "__main__":
    Game()