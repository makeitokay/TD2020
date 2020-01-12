import logging

logging.basicConfig(level=logging.DEBUG)

GAME_NAME = 'TD2020'

FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 650

GAME_FIELD_CELL_SIZE = 50
GAME_FIELD_WIDTH = SCREEN_WIDTH // GAME_FIELD_CELL_SIZE - 10
GAME_FIELD_HEIGHT = SCREEN_HEIGHT // GAME_FIELD_CELL_SIZE - 2

RIGHT_BLOCK_X = GAME_FIELD_WIDTH * GAME_FIELD_CELL_SIZE

SPRITE_GROUPS = [
    "all",

    "platforms",
    "weapon_platforms",
    "spawn",
    "base",
    "road",

    "text",

    "weapons",
    "base_weapons",

    "weapon_shop_objects"
]
