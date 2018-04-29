from src.const import *
from src.game_objects.dynamic.player import Player
from src.menu import Menu


class Camera:
    raw_warp_charge_image = load_image_folder("../gfx/warp_charge")[0]
    scaling = (3, 3)
    scaled_size = raw_warp_charge_image.get_width() * scaling[0], raw_warp_charge_image.get_height() * scaling[1]
    warp_charge_image = pygame.transform.scale(raw_warp_charge_image, scaled_size)
    
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.x, self.y = self.rect.center
        self.follow_target = None
        self.font = pygame.font.Font('src//font//font.otf', 30)
        
        self.menu = Menu(self.game)

        self._no_charge_error_counter = 0

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
        self.draw_fps()
        self.draw_warp_charges()
        
        if self._no_charge_error_counter > 0:
            self._no_charge_error()
            self._no_charge_error_counter -= 1
        
        # draw menu if game paused
        if self.game.paused:
            self.menu.update()
            self.menu.draw()
        
    def draw_fps(self):
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
    
    def draw_warp_charges(self):
        left_margin = 20
        top_margin = 20
        
        last_left = left_margin
        player = find_closest(self, Player)
        for i in range(player.warp_charges):
            image = Camera.warp_charge_image
            rect = image.get_rect()
            rect.topleft = (last_left, top_margin)
            self.game.surface.blit(image, rect)
            last_left += rect.w
    
    def no_charge_error(self):
        self._no_charge_error_counter = 20
        
    def _no_charge_error(self):
        left_margin = 20
        top_margin = 20
    
        error_surf = Camera.warp_charge_image.copy()
        error_surf.set_alpha(50)
        error_rect = error_surf.get_rect()
        x_surf = self.font.render("X", True, RED)
        x_rect = x_surf.get_rect()
        x_rect.center = error_rect.center
        error_surf.blit(x_surf, x_rect)
    
        error_rect.topleft = (left_margin, top_margin)
        
        self.game.surface.blit(error_surf, error_rect)