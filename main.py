import logging
import os
import random
import sys

from src.camera import Camera

import pygame
from pygame.locals import *
from src.const import *
from src.game_objects.dumb_enemy import DumbEnemy
from src.game_objects.follower import Follower
from src.game_objects.ground import Ground
from src.game_objects.player import Player
from src.game_objects.goal import Goal
from src.game_objects.warp_consumable import WarpConsumable


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
        
        self.fps_clock = pygame.time.Clock()
        self.events = pygame.event.get()
        
        screen = pygame.Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.camera = Camera(screen)
        self.world = "one"
        
        self.build_test_level()
        self.level = self.build_test_level
        
        self.reset = False
        self.run()
        while self.reset:
            self.reset_game()
            self.build_test_level()
            self.run()
    
    def run(self):
        running = True
        while running:
            self.surface.fill(L_OLIVE)

            if pygame.event.peek(pygame.QUIT):
                pygame.quit()
                sys.exit()

            self.events = pygame.event.get()

            self.update_all_sprites()
            self.draw_all_sprites()

            pygame.display.update()
            self.fps_clock.tick(FPS)
            if self.reset:
                break

    def update_all_sprites(self):
        for sprite in self.entities[ALL_SPRITES]:
            if sprite.world is None or sprite.world == self.world:
                sprite.update()
    
    def draw_all_sprites(self):
        # Draw based on depth
        sorted_by_depth = sorted(self.entities[ALL_SPRITES],
                                 key=lambda sprite: sprite.depth,
                                 reverse=True)
        for sprite in sorted_by_depth:
            if sprite.world != self.world and self.world is not None:
                sprite.draw()
        for sprite in sorted_by_depth:
            if sprite.world == self.world or sprite.world is None:
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

    def build_test_level(self):
        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
    
        player = Player(self, pos=(200, 200))
        self.add_entity(player, "one")
        
        bottom_left_pos = (0, 500)
        width = 13

        # Left guard
        build_row(Ground,
                  self,
                  (bottom_left_pos[0], bottom_left_pos[1] - Ground.height),
                  (0, -Ground.height),
                  3,
                  ["one", "two"])
        # Floor
        build_row(Ground,
                  self,
                  (bottom_left_pos[0], bottom_left_pos[1]),
                  (Ground.height, 0),
                  width,
                  ["one", "two"])
        # Right guard
        build_row(Ground,
                  self,
                  (bottom_left_pos[0] + (width-1) * Ground.width, bottom_left_pos[1] - Ground.height),
                  (0, -Ground.height),
                  3,
                  ["one", "two"])
        
        build_row(Ground,
                  self,
                  (bottom_left_pos[0] + Ground.width * 8, bottom_left_pos[1] - Ground.height),
                  (0, -Ground.height),
                  3,
                  ["two"])
        # Goal
        build_row(Goal,
                  self,
                  (bottom_left_pos[0] + (width - 2) * Ground.height,
                   bottom_left_pos[1] - Ground.height),
                  (0, 0),
                  1,
                  ["one", "two"])
        
        # Enemy
        enemy = Follower(self, pos=(bottom_left_pos[0] + Ground.width * 9, bottom_left_pos[1] - Ground.height))
        self.add_entity(enemy, "one")

        warp = WarpConsumable(self, pos=(700, 200))
        self.add_entity(warp)
        
    def reset_game(self):
        self.reset = False
        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
        player = Player(self, pos=(200, 200))
        self.add_entity(player)
        self.level()

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
