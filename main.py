import logging
import os
import random
import sys

from src.camera import Camera

import pygame
from pygame.locals import *
from src.const import *
from src.game_objects.ground import Ground
from src.game_objects.player import Player


class Game:
    
    def __init__(self):
        # Intializing Pygame window
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
        
        self.world = "one"
        
        player = Player(self, pos=(200, 200))
        self.add_entity(player)
        
        for i in range(7):
            ground = Ground(self, pos=(i * Ground.width + Ground.width / 2,
                                       DISPLAY_HEIGHT - Ground.height / 3))
            self.add_entity(ground, "one")
            
            if i == 4:
                ground = Ground(self, pos=(i * Ground.width + Ground.width / 2,
                                           DISPLAY_HEIGHT - Ground.height * 4 / 3))
                self.add_entity(ground, "two")
        
        self.run()
    
    def run(self):
        while True:
            self.surface.fill(L_GREY)

            if pygame.event.peek(pygame.QUIT):
                pygame.quit()
                sys.exit()

            self.events = pygame.event.get()

            self.update_all_sprites()
            self.draw_all_sprites()

            pygame.display.update()
            self.fps_clock.tick(FPS)

    def update_all_sprites(self):
        for sprite in self.entities[ALL_SPRITES]:
            sprite.update()
    
    def draw_all_sprites(self):
        # Draw based on depth
        for sprite in sorted(self.entities[ALL_SPRITES],
                             key=lambda sprite: sprite.depth,
                             reverse=True):
            sprite.draw()
    
    def add_entity(self, entity, world=None):
        # Tag it with world
        entity.world = None if world is None else world
        
        # Add entity to class's sprite group
        class_name = entity.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(entity)
        logging.info(f"{entity} created")
        
        # Also add to global sprite group
        self.entities[ALL_SPRITES].add(entity)
        


if __name__ == "__main__":
    Game()
