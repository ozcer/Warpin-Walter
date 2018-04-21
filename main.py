import logging
import os
import random
import sys
import pygame

from src.camera import Camera

from pygame.locals import *
from src.const import *
from src.levels.levels import LEVELS


class Game:
    
    def __init__(self):
        # Initializing Pygame window
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
        self.camera = Camera(self, screen)
        
        self.background_color = None
        self.levels = iter(LEVELS)
        self.build_next_level()
        self.run()

    def run(self):
        running = True
        while running:
            self.background_color = MAROON if self.world == "one" else D_GREY

            # TODO temp hack to update camera, prolly should systemize
            self.camera.update()
            self.surface.fill(self.background_color)
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
            if self.is_active(sprite):
                sprite.update()
    
    def draw_all_sprites(self):
        # Draw based on depth
        sorted_by_depth = sorted(self.entities[ALL_SPRITES],
                                 key=lambda sprite: sprite.depth,
                                 reverse=True)
        for sprite in sorted_by_depth:
            if not self.is_active(sprite):
                sprite.draw()
        for sprite in sorted_by_depth:
            if self.is_active(sprite):
                sprite.draw()
        self.camera.draw_ui()
    
    def is_active(self, sprite):
        return sprite.world == self.world or sprite.world is None
    
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
    
    def build_level(self, level):
        self.world = "one"
        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
        self.level = level
        self.level(self)
    
    def build_next_level(self):
        next_level = next(self.levels)
        self.build_level(next_level)
    
    def reset_level(self):
        self.build_level(self.level)

    def change_world(self):
        self.world = "one" if self.world == "two" else "two"

    @staticmethod
    def exit_game(message=EXIT_MESSAGE, log=False):
        if log:
            logging.info(message)
        else:
            print(message)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
        Game()
