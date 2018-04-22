import pygame
import logging
from math import cos, sin

from pygame.locals import *

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
        
        self.menu_surface = pygame.Surface((200, 150))
        self.menu_rect = self.menu_surface.get_rect()
        self.menu_options = ["Play", "Quit"]
        self.selection_index = 0
        
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
        
        if self.game.level("name") != "menu background":
            warp_charges = player.warp_charges
            world = 2 if self.game.world == "two" else 1
            warp_text = f"WARPS: "
            world_text = f"LEVEL: "
            warp_color = L_BLUE if warp_charges > 0 else RED
            world_color = RED if world == 1 else BLACK
            warp_surface = self.font.render(warp_text, False, BLACK)
            world_surface = self.font.render(world_text, False, BLACK)
            warp_num_surface = self.font.render(str(warp_charges), False, warp_color)
            world_num_surface = self.font.render(str(self.game.level("name")), False, world_color)
            xmargin = 20
            ymargin = 20
            world_x = 95 + xmargin
            warp_x = 120 + xmargin
    
            self.game.surface.blit(world_surface, (xmargin, ymargin))
            self.game.surface.blit(warp_surface, (xmargin, 30 + ymargin))
            self.game.surface.blit(world_num_surface, (world_x, 1 + ymargin))
            self.game.surface.blit(warp_num_surface, (warp_x, 30 + ymargin))

        if self.game.paused:
            self.menu_rect.center = DISPLAY_WIDTH/2 , DISPLAY_HEIGHT/2 - 150
            self.menu_surface.fill(D_BLUE)

            #menu_surface.set_colorkey((0, 0, 0))
            self.menu_surface.set_alpha(155)
            
            self.game.surface.blit(self.menu_surface, self.menu_rect)
            
            # draw options
            x = self.menu_rect.centerx
            dy = self.menu_rect.h / (len(self.menu_options) + 1)
            for index, option in enumerate(self.menu_options):
                if option == "Play" and not self.game.level("name") == "menu background":
                    option = "Resume"
                option_surface = self.font.render(option, False, BLACK)
                _rect = option_surface.get_rect()
                _rect.center = x, self.menu_rect.top + (index +1 )* dy
                
                if index == self.selection_index:
                    # selected background
                    bg_surf = pygame.Surface((150, 40))
                    bg_rect = bg_surf.get_rect()
                    bg_rect.center = x, self.menu_rect.top + (index +1 ) * dy
                    bg_surf.fill(L_GREY)
                    bg_surf.set_alpha(155)
    
                    self.game.surface.blit(bg_surf, bg_rect)
                self.game.surface.blit(option_surface, _rect)
            
            for event in self.game.events:
                if event.type == KEYDOWN:
                    key = event.key
                    if key == K_UP:
                        self.selection_index -= 1
                    elif key == K_DOWN:
                        self.selection_index -= 1
                    elif key == K_RETURN:
                        if self.selection_index == 0:
                            self.game.paused = False
                            if self.game.level("name") == "menu background":
                                self.game.build_next_level()
                        elif self.selection_index == 1:
                            self.game.exit_game("Goodbye")
                        
                    self.selection_index = self.selection_index % len(self.menu_options)
