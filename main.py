import logging
import os
import random
import sys

import pygame
from pygame.locals import *
from src.const import *



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
        
        self.run()
    
    def run(self):
        while True:
            self.surface.fill(L_GREY)
            
            self.update_all_sprites()
            self.draw_all_sprites()

            # fps and update display
            pygame.display.update()
            self.fps_clock.tick(FPS)
            
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    
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
    
    def add_entity(self, object):
        # add to its own sprite group
        class_name = object.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(object)
        logging.info(f"{object} created")
        
        # also add to global sprite group
        self.entities[ALL_SPRITES].add(object)
    

if __name__ == "__main__":
    Game()