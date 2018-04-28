import logging
import sys
import time
import itertools

from pygame.locals import *

from src.const import *
from src.level.main_menu import MainMenu
from src.sound_manager import SoundManager


class Game:
    logging.basicConfig(level=LOG_LEVEL,
                        datefmt='%m/%d/%Y %I:%M:%S%p',
                        format='%(asctime)s %(message)s')
    
    def __init__(self):
        # Initializing Pygame window
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()
        pygame.init()
        
        pygame.display.set_caption(CAPTION)
        self.surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
        
        # Import here to avoid
        # pygame.error: cannot convert without pygame.display initialized
        from src.camera import Camera
        from src.level.tutorial_one import TutorialOne
        from src.level.main_menu import MainMenu
        from src.level.tutorial_two import TutorialTwo

        levels = [MainMenu, TutorialOne, TutorialTwo]
        
        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
        self.fps_clock = pygame.time.Clock()
        self.events = pygame.event.get()
        
        screen = pygame.Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.camera = Camera(self, screen)
        self.font = pygame.font.Font('src//font//font.otf', 30)

        self.sfxs = SoundManager()
        
        self.background_color = None
        self.levels = itertools.cycle(levels)
        self.build_next_level()

        self.paused = True
        self.run()

    def run(self):
        
        while True:
            self.background_color = MAROON if self.world == "one" else D_GREY

            # TODO temp hack to update camera, prolly should systemize
            self.camera.update()
            self.surface.fill(self.background_color)
            if pygame.event.peek(pygame.QUIT):
                pygame.quit()
                sys.exit()

            self.events = pygame.event.get()
            
            
            self.update_all_sprites()
            self.draw_all_sprites()

            for event in self.events:
                if event.type == KEYDOWN:
                    key = event.key
                    if key == pygame.K_ESCAPE:
                        self.paused = not self.paused

            pygame.display.update()
            self.fps_clock.tick(FPS)
            
    def update_all_sprites(self):
        for sprite in self.entities[ALL_SPRITES]:
            if self.is_active(sprite):
                sprite.update()
    
    def draw_all_sprites(self):
        # Draw based on depth
        sorted_by_depth = sorted(self.entities[ALL_SPRITES],
                                 key=lambda sprite: sprite.depth,
                                 reverse=True)
        for sprite in sorted_by_depth:
            if not self.is_active(sprite):
                sprite.draw()
        for sprite in sorted_by_depth:
            if self.is_active(sprite):
                sprite.draw()
        self.camera.draw_ui()
    
    def is_active(self, sprite):
        return sprite.world == self.world or sprite.world is None
    
    def add_entity(self, entity, world=None):
        # Tag it with world
        if world is None:
            self.both_world_entities.add(entity)
        entity.world = "one" if world is None else world
        
        # Add entity to class's sprite group
        class_name = entity.__class__.__name__
        if class_name not in self.entities:
            self.entities[class_name] = pygame.sprite.Group()
        self.entities[class_name].add(entity)
        logging.info(f"{entity} created")
        
        # Also add to global sprite group
        self.entities[ALL_SPRITES].add(entity)
    
    def draw_menu(self):
        self.menu.draw()
        
    def build_level(self, level):
        self.world = "one"
        self.entities = {ALL_SPRITES: pygame.sprite.Group()}
        self.both_world_entities = pygame.sprite.Group()
        self.level = level
        
        # brief seconds to show level name
        if not isinstance(self.level, MainMenu):
            level_surface = self.font.render(self.level.name, False, WHITE)
            self.surface.fill(BLACK)
            self.surface.blit(level_surface, (0, 0))
            pygame.display.update()
            time.sleep(0)
            
        self.level.build()
    
    def build_next_level(self):
        next_level_cls = next(self.levels)
        next_level = next_level_cls(self)
        self.build_level(next_level)
    
    def reset_level(self):
        self.build_level(self.level)

    def change_world(self):
        self.world = "one" if self.world == "two" else "two"
        for entity in self.both_world_entities:
            entity.world = self.world

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
