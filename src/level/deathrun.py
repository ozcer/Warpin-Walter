from src.const import *
from src.game_objects.dynamic.chaser import Chaser
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.goal import Goal
from src.game_objects.interactible.warp_consumable import WarpCharge
from src.game_objects.terrain.background_block import BackgroundBlock
from src.game_objects.terrain.ground import Ground
from src.game_objects.terrain.platform import Platform
from src.level.level import Level


class DeathRun(Level):
    
    def __init__(self, game):
        name = "Raining Slimes and Slimes".title()
        super().__init__(game, name=name)
    
    def build(self):
        bottom_left_pos = (0, 0)
        room_width = 30
        room_height = 9
        
        fall_height = 14
        fall_width = 10
        
        pit_width = 3
        pit_height = 2
        
        eroom_start = 8
        eroom_width = 10
        
        step_width = 4
        
        spawn = get_end_pos(Ground, bottom_left_pos, (3, 10), up=True)
        player = Player(self.game, pos=spawn, warp_charges=0)
        self.game.add_entity(player, "one")
        self.game.camera.follow(player)
        
        # falling ene
        pos = get_end_pos(Ground, spawn, (1, 15), up=True)
        build_array(Chaser, self.game, pos, (2, 1), world="one")

        pos = get_end_pos(Ground, spawn, (1, 15), up=True)
        #build_array(Chaser, self.game, pos, (2, 1), world="two")
        
        pos = get_end_pos(Ground, spawn, (9, 35), up=True)
        build_array(Chaser, self.game, pos, (1, 1), world="two")
        
        
        # Left Guard
        top_left_pos = build_column(Ground, self.game, bottom_left_pos, fall_height, up=True)
        
        
        # Background
        build_array(BackgroundBlock, self.game, bottom_left_pos, (room_width, room_height), up=True, world="three")
        # fall bg
        build_array(BackgroundBlock, self.game, top_left_pos, (fall_width, fall_height-room_height), world="three")
        
        # pit
        spawn = get_end_pos(Ground, bottom_left_pos, (1, 2),)
        pit_bl = build_column(Ground, self.game, spawn, pit_height)

        spawn = get_end_pos(Ground, pit_bl, (2, 1), )
        pit_br = build_row(Ground, self.game, spawn, pit_width+1)
        
        spawn = get_end_pos(Ground, pit_br, (1, 2), up=True)
        pit_tr = build_column(Ground, self.game, spawn, pit_height, up=True)
        
        spawn = get_end_pos(Ground, pit_bl, (2, 2), up=True)
        build_array(BackgroundBlock, self.game, spawn, (pit_width, pit_height-1), up=True, world="three")
        
        # pit charge
        pos = get_end_pos(Ground, pit_bl, ((pit_width + 1) // 2 + 1, 2), up=True)
        build_array(WarpCharge, self.game, pos, (1, 1))
        
        
        # Floor
        bottom_right_pos = build_row(Ground, self.game, pit_tr, room_width-pit_width)

        # Right Guard
        build_column(Ground, self.game, bottom_right_pos, room_height, up=True)
        
        
        # eroom1
        pos = get_end_pos(Ground, pit_tr, (eroom_start, 2), up=True)
        build_column(Ground, self.game, pos, 3, up=True, world="one")

        pos = get_end_pos(Ground, pit_tr, (eroom_start + eroom_width, 2), up=True)
        wall2_end = build_column(Ground, self.game, pos, 3, up=True, world="one")
        
        pos = get_end_pos(Ground, wall2_end, (3, 4), left=True, up=True)
        build_array(WarpCharge, self.game, pos, (1, 1))

        eroom_end_base = get_end_pos(Ground, pit_tr, (eroom_start + eroom_width - 3, 2), up=True)
        build_array(DumbEnemy, self.game, eroom_end_base, (2, 1), up=True, world="two")
        
        # middle plat
        pos = get_end_pos(Ground, wall2_end, (6, 2), left=True, up=True)
        mid_plat = build_array(Platform, self.game, pos, (1, 1), world="two")

        pos = get_end_pos(Ground, mid_plat, (3, 4), left=True, up=True)
        build_array(WarpCharge, self.game, pos, (1, 1))
        
        
        # nump
        pos = get_end_pos(Ground, bottom_right_pos, (2, 2), left=True, up=True)
        bump = build_array(Ground, self.game, pos, (1, 2), up=True, world="one")
        
        # bump charge
        build_array(WarpCharge, self.game, pos, (1, 1), world="two")
        
        # bump guarder
        pos = get_end_pos(Ground, bump, (1, 2), left=True, up=True)
        build_array(Chaser, self.game, pos, (1, 1), world="one")
        
        
        
        # first plat
        pos = get_end_pos(Ground, bump, (3, 3), left=True, up=True)
        build_array(Platform, self.game, pos, (1, 1), world="two")

        pos = get_end_pos(Ground, bump, (3, 4), left=True, up=True)
        build_array(WarpCharge, self.game, pos, (1, 1))

        pos = get_end_pos(Ground, bump, (6, 6), left=True, up=True)
        build_array(WarpCharge, self.game, pos, (1, 1))
        
        # victory plat
        pos = get_end_pos(Ground, pit_tr, (3, 5), up=True)
        vic_plat = build_array(Ground, self.game, pos, (1, 1))
        pos = get_end_pos(Ground, vic_plat, (1, 2), up=True)
        build_array(Goal, self.game, pos, (1, 1))
