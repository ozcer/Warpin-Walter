import pygame
from math import cos, sin

from src.const import *


class Camera():
    
    def __init__(self, rect):
        self.rect = rect
        self.x, self.y = self.rect.center
        self.follow_target = None
        
    def follow(self, target):
        self.follow_target = target
    
    def update(self):
        self.rect.center = self.x, self.y
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

