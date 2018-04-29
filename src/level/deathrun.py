from src.const import *
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.goal import Goal
from src.game_objects.interactible.warp_consumable import WarpCharge
from src.game_objects.terrain.background_block import BackgroundBlock
from src.game_objects.terrain.ground import Ground
from src.level.level import Level


class DeathRun(Level):
    
    def __init__(self, game):
        name = "Gotta Go Fast".title()
        super().__init__(game, name=name)
    
    def build(self):
        bottom_left_pos = (0, 0)
        room_width = 40
        room_height = 14
        
        pos = get_end_pos(Ground, bottom_left_pos, (3, 10), yreverse=True)
        player = Player(self.game, pos=pos, warp_charges=10)
        self.game.add_entity(player, "one")
        self.game.camera.follow(player)
        
        # Floor
        bottom_right_pos = build_row(Ground, self.game, bottom_left_pos, room_width)
        
        # Left Guard
        top_left_pos = build_column(Ground, self.game, bottom_left_pos, room_height, reverse=True)
        # Right Guard
        build_column(Ground, self.game, bottom_right_pos, room_height, reverse=True)
        
        # Ceiling
        #top_right_pos = build_row(Ground, self.game, top_left_pos, room_width)
        
        # Background
        build_array(BackgroundBlock, self.game, top_left_pos, (room_width, room_height), world="three")
        
        # Ennemy
        spawn_pos = get_end_pos(Ground, bottom_left_pos, (8, 2), yreverse=True)
        enemy = DumbEnemy(self.game, pos=spawn_pos)
        self.game.add_entity(enemy, "one")
        