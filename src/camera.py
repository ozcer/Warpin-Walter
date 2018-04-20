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
        self.font = pygame.font.SysFont('Arial', 30)
        self.font.set_bold(True)
        
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

    def draw_ui(self, color=BLACK):
        if not hasattr(self, "player"):
            self.get_player()

        warp_charges = self.player.warp_charges
        world = 2 if self.game.world == "two" else 1
        warp_text = f"WARPS: {warp_charges}"
        world_text = f"WORLD: {world}"
        warpsurface = self.font.render(warp_text, False, color)
        worldsurface = self.font.render(world_text, False, color)

        self.game.surface.blit(worldsurface, (0, 0))
        self.game.surface.blit(warpsurface, (0, 30))

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