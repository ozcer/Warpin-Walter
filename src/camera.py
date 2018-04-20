import pygame
import logging
from math import cos, sin

from src.const import *
from src.game_objects.dynamic.player import Player


class Camera:
    
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.x, self.y = self.rect.center
        self.follow_target = None
        self.font = pygame.font.Font('src//font//font.otf', 30)
        #self.font.set_bold(True)
        
    def follow(self, target):
        self.follow_target = target
    
    def update(self):
        self.rect.center = self.x, self.y - 50
        if self.follow_target:
            self.x, self.y = self.follow_target.x, self.follow_target.y

    def adjust_rect(self, raw_rect):
        """
        given rect, return adjusted rect offset by camera
        :param raw_rect: Rect
        :return: Rect
        """
        width, height = raw_rect.w, raw_rect.h
        left = raw_rect.left - self.rect.left
        top = raw_rect.top - self.rect.top
        adjusted = pygame.Rect(left, top, width, height)
        return adjusted

    def adjust_point(self, p):
        """
        given point, return adjusted point offset by camera
        :param p: (int, int)
        :return: (int, int)
        """
        x = p[0] - self.rect.topleft[0]
        y = p[1] - self.rect.topleft[1]
        return x, y

    def draw_ui(self):
        if not hasattr(self, "player"):
            self.get_player()

        warp_charges = self.player.warp_charges
        world = 2 if self.game.world == "two" else 1
        warp_text = f"WARPS: "
        world_text = f"WORLD: "
        warp_color = L_BLUE if warp_charges > 0 else RED
        world_color = RED if world == 1 else BLACK
        warp_surface = self.font.render(warp_text, False, BLACK)
        world_surface = self.font.render(world_text, False, BLACK)
        warp_num_surface = self.font.render(str(warp_charges), False, warp_color)
        world_num_surface = self.font.render(str(world), False, world_color)
        world_x = 125
        warp_x = 120

        self.game.surface.blit(world_surface, (0, 0))
        self.game.surface.blit(warp_surface, (0, 30))
        self.game.surface.blit(world_num_surface, (world_x, 1))
        self.game.surface.blit(warp_num_surface, (warp_x, 30))

    def get_player(self):
        """
        Gets the player if we do not already have one, raises an error if there is no player
        :return Player:
        """
        player_class = Player.__class__.__name__
        if isinstance(self.follow_target, Player):
            self.player = self.follow_target
        elif len(self.game.entites[player_class]) == 1:
            self.player = self.game.entities[player_class][0]
        elif len(self.game.entites[player_class]) == 1:
            self.player = self.game.entities[player_class][0]
            logging.info("Cannot be certain that this is actually the correct player.")
        else:
            raise AssertionError