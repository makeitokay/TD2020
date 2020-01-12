import pygame as pg
from core.utils import load_level
from core.settings import GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT

from core.objects.platforms import load_platform, Spawn

from .field import Field


class GameField(Field):
    WIDTH = GAME_FIELD_WIDTH
    HEIGHT = GAME_FIELD_HEIGHT

    CELL_STROKE_IMAGE = "game_field_cell_stroke.png"

    SPRITE_GROUPS = ["platforms", "weapons"]

    def __init__(self, game, pos, level=1):
        super().__init__(game, pos)

        self.level = level

    def init_level(self):
        level = load_level(self.level)
        for i in range(len(level)):
            for j in range(len(level[i])):
                platform = load_platform(self.game, level[i][j], (j, i))
                self.field[i][j] = platform

                if isinstance(platform, Spawn):
                    platform.set_level(self.level)

    def set_weapon(self, weapon_class):
        x, y = self.selected_cell
        self.field[y][x] = weapon_class(self.game, (x, y))

    def get_spawn_platform(self):
        for row in self.field:
            for platform in row:
                if isinstance(platform, Spawn):
                    return platform