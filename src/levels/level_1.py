import pygame

from src.const import *
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.follower import Follower
from src.game_objects.interactible.goal import Goal
from src.game_objects.terrain.ground import Ground
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.warp_consumable import WarpConsumable
from src.game_objects.interactible.warp_switch import WarpSwitch


def level_1(game):
    player = Player(game, pos=(200, 200))
    game.add_entity(player, "one")
    game.camera.follow(player)
    bottom_left_pos = (0, 500)
    width = 13

    # Left guard
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              ["one", "two"])
    # Floor
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1]),
              (Ground.height, 0),
              width,
              ["one", "two"])
    # Right guard
    build_row(Ground,
              game,
              (bottom_left_pos[0] + (width - 1) * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              ["one", "two"])

    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 8, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              ["two"])
    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              ["one", "two"])

    # Enemy
    enemy = Follower(game, pos=(bottom_left_pos[0] + Ground.width * 9, bottom_left_pos[1] - Ground.height))
    game.add_entity(enemy, "one")

    warp = WarpConsumable(game, pos=(700, 200))
    game.add_entity(warp)