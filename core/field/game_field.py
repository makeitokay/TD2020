import pygame as pg
from core.utils import load_level
from core.settings import GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT

from core.objects.platforms import load_platform

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
                self.field[i][j] = load_platform(self.game, level[i][j], (j, i))