import pygame
import logging
from math import cos, sin

from pygame.locals import *

from src.const import *
from src.game_objects.dynamic.player import Player
from src.menu import Menu


class Camera:
    
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.x, self.y = self.rect.center
        self.follow_target = None
        self.font = pygame.font.Font('src//font//font.otf', 30)
        #self.font.set_bold(True)
        
        self.menu = Menu(self.game)
        
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
        player = find_closest(self, Player)
        
        fps = int(self.game.fps_clock.get_fps())
        if fps >= 58:
            color = GREEN
        elif fps >= 53:
            color = ORANGE
        else:
            color = RED
        fps_surface = self.font.render(str(fps), True, color)
        fps_rect = fps_surface.get_rect()
        fps_rect.topright = (DISPLAY_WIDTH, 0)
        self.game.surface.blit(fps_surface, fps_rect)
        
        if self.game.paused:
            self.menu.update()
            self.menu.draw()

