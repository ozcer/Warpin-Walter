import pygame


class Camera():
    
    def __init__(self, rect):
        
        self.rect = rect
    
    def adjust_rect(self, raw_rect):
        """
        given rect, return adjusted rect offset by camera
        :param raw_rect: Rect
        :return: Rect
        """
        width, height = raw_rect.w, raw_rect.h
        left = raw_rect.left + self.rect.left
        top = raw_rect.top + self.rect.top
        adjusted = pygame.Rect(left, top, width, height)
        
        return adjusted