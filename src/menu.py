

from pygame.locals import *
from src.const import *


class Menu:
    
    def __init__(self, game):
        self.game = game
        self.image = pygame.Surface((200, 200))
        self.rect = self.image.get_rect()
        self.options = ["Play", "Controls", "Quit"]
        self.selection_index = 0
        
        self.x = DISPLAY_WIDTH / 4
        self.y = DISPLAY_HEIGHT / 2 - 150
        self.rect.center = self.x, self.y

        self.font = pygame.font.Font('src//font//font.otf', 30)
        
    def update(self):
        self.rect.center = self.x, self.y
        self._process_input()
    
    def draw(self):
        self.image.fill(D_BLUE)
        self.image.set_alpha(155)
        self.game.surface.blit(self.image, self.rect)
        
        self._draw_options()
        
    def _draw_options(self):
        # draw options
        dy = self.rect.h / (len(self.options) + 1)
        for index, option in enumerate(self.options):
            # Resume becomes Play if game never started
            if option == "Play" and not self.game.level("name") == "menu background":
                option = "Resume"
            
            option_surface = self.font.render(option, False, BLACK)
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
                if key == K_UP:
                    self._change_selection(-1)
                elif key == K_DOWN:
                    self._change_selection(1)
                elif key == K_RETURN:
                    self._make_selection()
        
    def _change_selection(self, change):
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
            pass

        elif self.selection_index == 2:
            self.game.exit_game()
    
    def __str__(self):
        return f"{self.__class__.__name__} at {self.x, self.y}"
