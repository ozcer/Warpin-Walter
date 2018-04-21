import pygame

from src.const import *
from src.game_objects.dynamic.dumb_enemy import DumbEnemy
from src.game_objects.dynamic.follower import Follower
from src.game_objects.interactible.goal import Goal
from src.game_objects.interactible.warp_switch import WarpSwitch
from src.game_objects.terrain.ground import Ground
from src.game_objects.terrain.kill_field import KillField
from src.game_objects.dynamic.player import Player
from src.game_objects.interactible.warp_consumable import WarpConsumable


def level_1(game):
    player = Player(game, pos=(200, 9500), warp_charges=0)
    game.add_entity(player, "one")
    game.camera.follow(player)
    bottom_left_pos = (0, 10000)
    width = 20

    # Secret platform
    build_row(Ground,
              game,
              (bottom_left_pos[0] - Ground.width * 4,
               bottom_left_pos[1] - Ground.width * 2),
              (Ground.height, 0),
              3,
              None)
    warp = WarpConsumable(game, pos=(bottom_left_pos[0] - Ground.width * 4, bottom_left_pos[1] - Ground.width * 3))
    game.add_entity(warp)

    # Platform 1
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1] - Ground.width * 4),
              (Ground.height, 0),
              3,
              None)

    # Platform 2
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 4, bottom_left_pos[1] - Ground.width * 4),
              (Ground.height, 0),
              3,
              None)

    # Platform 2 false extension
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.height * 7, bottom_left_pos[1] - Ground.width * 4),
              (Ground.height, Ground.height),
              3,
              "two")

    # Platform 3 "one" 1
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.height * 9, bottom_left_pos[1] - Ground.width * 5),
              (Ground.height, 0),
              2,
              None)


    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              None)


def level_2(game):
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
              None)
    # Floor
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1]),
              (Ground.height, 0),
              width,
              None)
    # Right guard
    build_row(Ground,
              game,
              (bottom_left_pos[0] + (width - 1) * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              None)

    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 8, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              "two")
    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              None)

    # Enemy
    enemy = Follower(game, pos=(bottom_left_pos[0] + Ground.width * 9, bottom_left_pos[1] - Ground.height))
    game.add_entity(enemy, "one")

    warp = WarpConsumable(game, pos=(700, 200))
    game.add_entity(warp)
    return "Bee"


def level_3(game):
    player = Player(game, pos=(75, 400), warp_charges=1)
    game.add_entity(player, "one")
    game.camera.follow(player)
    bottom_left_pos = (0, 500)
    width = 8

    # Left guard
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              5,
              None)
    # Floor
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1]),
              (Ground.height, 0),
              width,
              None)
    # Ceiling
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 3, bottom_left_pos[1] - Ground.height * 2),
              (Ground.width, 0),
              width - 3,
              None)

    # Ceiling false block
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1] - Ground.width * 2),
              (Ground.height, 0),
              width,
              "one")

    # Right guard
    build_row(Ground,
              game,
              (bottom_left_pos[0] + (width - 1) * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              5,
              None)

    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * (width - 3), bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              2,
              "two")
    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              None)

    # Enemy
    enemy = Follower(game, pos=(bottom_left_pos[0] + Ground.width * 6, bottom_left_pos[1] - Ground.height))
    game.add_entity(enemy, "one")

    warp = WarpConsumable(game, pos=(500, 200))
    game.add_entity(warp)
    return "Look ahead, think behind."


def level_4(game):
    player = Player(game, pos=(200, 200), warp_charges=1)
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
              None)
    # Floor
    build_row(Ground,
              game,
              (bottom_left_pos[0], bottom_left_pos[1]),
              (Ground.height, 0),
              width - 1,
              None)

    # Stack of enemies
    build_row(DumbEnemy,
              game,
              (bottom_left_pos[0] + (width - 4) * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              8,
              "one")

    # Blocking pillar
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 6, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              3,
              "two")
    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              None)

    return "Just keep moving!"


def level_5(game):
    player = Player(game, pos=(600, 0), warp_charges=0)
    game.add_entity(player, "one")
    game.camera.follow(player)
    bottom_left_pos = (0, 25000)
    width = 50
    backtrack = 15

    # Left guard
    build_row(Ground,
              game,
              (bottom_left_pos[0] - backtrack * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              15,
              None)
    # Floor
    build_row(Ground,
              game,
              (bottom_left_pos[0] - backtrack * Ground.width, bottom_left_pos[1]),
              (Ground.height, 0),
              width + backtrack,
              None)

    # Stack of enemies
    build_row(DumbEnemy,
              game,
              (bottom_left_pos[0] + (width - 4) * Ground.width, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              8,
              "one")

    # Hinting block
    build_row(Ground,
              game,
              (bottom_left_pos[0] + Ground.width * 1.9, bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              1,
              "two")
    # Goal
    build_row(Goal,
              game,
              (bottom_left_pos[0] + (width - 3) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, 0),
              1,
              None)

    # Right guard
    build_row(Ground,
              game,
              (bottom_left_pos[0] + (width - 2) * Ground.height,
               bottom_left_pos[1] - Ground.height),
              (0, -Ground.height),
              15,
              None)

    # Kill field
    build_row(KillField,
              game,
              (bottom_left_pos[0] - 20000, bottom_left_pos[1] + 300),
              (KillField.width, 0),
              20,
              None)

    warp = WarpConsumable(game, pos=(bottom_left_pos[0] - (backtrack * Ground.width) + 100,
                                     bottom_left_pos[1] - 100))
    game.add_entity(warp)

    return "The Oscar special."


LEVELS = [level_1, level_2, level_3, level_4, level_5]