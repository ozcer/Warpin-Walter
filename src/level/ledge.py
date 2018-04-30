from src.const import *
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.chaser import Chaser
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.goal import Goal
from src.game_objects.interactible.warp_consumable import WarpCharge
from src.game_objects.terrain.background_block import BackgroundBlock
from src.game_objects.terrain.ground import Ground
from src.game_objects.terrain.platform import Platform
from src.game_objects.terrain.sign import Sign
from src.level.level import Level


class Ledge(Level):
    
    def __init__(self, game):
        name = "Blue's Clues Finds You"
        super().__init__(game, name=name)
    
    def build(self):
        bottom_left_pos = (0, 1000)
        room_width = 20
        room_height = 17
        lower_ledge_pos = (int(room_width/2.5), 3.5)
        backwall_dim = (3, 4)
        back_ledge_width = 2

        pos = get_end_pos(Ground, bottom_left_pos, (3, 4), up=True)
        player = Player(self.game, pos=pos, warp_charges=0)
        self.game.add_entity(player, "one")
        self.game.camera.follow(player)
        
        # Floor
        bottom_right_pos = build_row(Ground, self.game, bottom_left_pos, room_width)
    
        # Left Guard
        top_left_pos = build_column(Ground, self.game, bottom_left_pos, room_height, up=True)
        # Right Guard
        build_column(Ground, self.game, bottom_right_pos, room_height, up=True)
    
        # Ceiling
        top_right_pos = build_row(Ground, self.game, top_left_pos, room_width)
    
        # Background
        build_array(BackgroundBlock, self.game, top_left_pos, (room_width, room_height), world="three")
        
        # back wall
        pos = get_end_pos(Ground, bottom_right_pos, (2,2), left=True, up=True)
        back_wall_end = build_array(Ground, self.game, pos, backwall_dim, left=True, up=True)
        
        # lower ledge
        pos = get_end_pos(Ground, bottom_left_pos, lower_ledge_pos, up=True)
        build_row(Platform, self.game, pos, 2, world="two")

        # back ledge
        pos = get_end_pos(Ground, back_wall_end, (2, 1), left=True)
        back_ledge_end = build_row(Ground, self.game, pos, back_ledge_width, left=True)
        
        # under ledge charge and enemy
        pos = get_end_pos(Ground, bottom_right_pos, (backwall_dim[0] + 2, 2), left=True, up=True)
        build_row(WarpCharge, self.game, pos, 1)
        build_row(DumbEnemy, self.game, pos, 1, world="one")

        # on backwall charge and enemy
        pos = get_end_pos(Ground, bottom_right_pos, (3, backwall_dim[1] + 2), left=True, up=True)
        build_row(WarpCharge, self.game, pos, 1)
        build_row(Chaser, self.game, pos, 1, world="two")
        
        # middle ledge
        pos = get_end_pos(Ground, back_ledge_end, (4, 3.7), up=True, left=True)
        middle_ledge_end = build_row(Platform, self.game, pos, 1, left=True, world="one")

        # mid air charge
        pos = get_end_pos(Ground, middle_ledge_end, (4, 4), left=True, up=True)
        build_row(WarpCharge, self.game, pos, 1)
        
        # victory ledge
        pos = get_end_pos(Ground, middle_ledge_end, (7, 1.7), left=True)
        flag_root = build_row(Ground, self.game, pos, 5, left=True, world="two")
        
        # goal
        pos = get_end_pos(Ground, flag_root, (1, 2), up=True)
        goal = Goal(self.game, pos=pos)
        self.game.add_entity(goal, world="two")