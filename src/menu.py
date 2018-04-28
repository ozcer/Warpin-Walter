

from pygame.locals import *
from src.const import *


class Menu:
    
    x = DISPLAY_WIDTH / 4
    y = DISPLAY_HEIGHT / 2 - 150
    width = 180
    height = 200
    
    controls_text = ("WASD - move\n"
                     "Space - warp\n"
                     "R - restart\n"
                     "Esc - pause\n")
    
    about_text = ("PyWeek April 2018 entry \n"
                  "by Oscar Lin and Anas Elmi\n\n"
                  "github.com/ozcer/warpin-walter\n")
    
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font('src//font//font.otf', 30)
        
        self.image = pygame.Surface((Menu.width, Menu.height))
        self.image.fill(D_BLUE)
        self.image.set_alpha(155)
        
        self.rect = self.image.get_rect()
        self.x, self.y = Menu.x, Menu.y
        self.rect.center = self.x, self.y
        
        self.options = ["Play", "Controls", "About"]
        self.selection_index = 0
        
        # Info panel
        self.panel_surf = pygame.Surface((Menu.width * 2, Menu.height))
        self.panel_rect = self.panel_surf.get_rect()
        self.panel_rect.left = self.rect.right + 10
        self.panel_rect.centery = self.y
        self.panel_surf.fill(L_BLUE)
        self.panel_surf.set_alpha(155)
        self.panel_on = False
        self.panel_text = ""
        self.panel_font = pygame.font.Font('src//font//font.otf', 20)
        
        
    def update(self):
        self.rect.center = self.x, self.y
        self._process_input()
    
    def draw(self):
        self.game.surface.blit(self.image, self.rect)
        
        if self.panel_on:
            self.game.surface.blit(self.panel_surf, self.panel_rect)
            self._show_panel(self.panel_text)
            
        self._draw_options()
        
    def _draw_options(self):
        # draw options
        dy = self.rect.h / (len(self.options) + 1)
        for index, option in enumerate(self.options):
            # Resume becomes Play if game never started
            if option == "Play" and not self.game.level("name") == "menu background":
                option = "Resume"
            
            option_surface = self.font.render(option, True, BLACK)
            option_rect = option_surface.get_rect()
            option_rect.center = self.rect.centerx, self.rect.top + (index + 1) * dy
            
            # selected highlight
            if index == self.selection_index:
                selected_surf = pygame.Surface((150, 40))
                selected_rect = selected_surf.get_rect()
                selected_rect.center = self.rect.centerx, self.rect.top + (index + 1) * dy
                selected_surf.fill(L_GREY)
                selected_surf.set_alpha(155)
            
                self.game.surface.blit(selected_surf, selected_rect)
            
            self.game.surface.blit(option_surface, option_rect)
    
    def _process_input(self):
        for event in self.game.events:
            if event.type == KEYDOWN:
                key = event.key
                if key in (K_UP, K_w):
                    self._change_selection(-1)
                elif key in (K_DOWN, K_s):
                    self._change_selection(1)
                elif key in (K_RETURN, K_SPACE):
                    self._make_selection()
        
    def _change_selection(self, change):
        self.panel_on = False
        
        self.selection_index += change
        self.selection_index = self.selection_index % len(self.options)
        
        selection = self.options[self.selection_index]
        logging.info(f"{self} selecting {selection} at index {self.selection_index}")
    
    def _make_selection(self):
        # Play/Resume
        if self.selection_index == 0:
            self.game.paused = False
            if self.game.level("name") == "menu background":
                self.game.build_next_level()
        
        elif self.selection_index == 1:
            self.panel_on = True
            self.panel_text = (Menu.controls_text)
        elif self.selection_index == 2:
            self.panel_on = True
            self.panel_text = (Menu.about_text)
    
    def _show_panel(self, text):
        left_padding = 10
        top_padding = 10
        
        last_top = self.rect.top + top_padding
        for index, line in enumerate(text.split("\n")):
            text_surf = self.panel_font.render(line, True, BLACK)
            text_rect = text_surf.get_rect()
            text_rect.topleft = (self.panel_rect.left + left_padding, last_top)
            self.game.surface.blit(text_surf, text_rect)
            
            last_top += text_rect.h

    def __str__(self):
        return f"{self.__class__.__name__} at {self.x, self.y}"
