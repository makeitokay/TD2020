import pygame as pg
from .utils import BLUE, BLACK, get_cell_coordinates, load_level
from .settings import FIELD_WIDTH, FIELD_HEIGHT, CELL_SIZE

from .objects.platforms import load_object
# from .objects.platforms.platform import Platform
# from .objects.platforms.weapon import Weapon
# from .objects.platforms.spawn import Spawn
# from .objects.platforms.base import Base
# from .objects.platforms.road import Road
from .objects.info import Info

class Field:
    WIDTH = FIELD_WIDTH
    HEIGHT = FIELD_HEIGHT

    def __init__(self, game, surface, level=1):
        self.game = game
        self.surface = surface
        self.level = level

        self.cells_rects = [[None] * self.WIDTH for _ in range(self.HEIGHT)]
        self.cells_objects = [[None] * self.WIDTH for _ in range(self.HEIGHT)]

        # self.cells_objects = load_level(self.game, 1)
        self.init_level()

        self.selected_cell = None

    def render(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                cell = pg.Rect(*get_cell_coordinates(j, i), CELL_SIZE, CELL_SIZE)
                self.cells_rects[i][j] = cell
                color = BLUE if (i, j) == self.selected_cell else BLACK
                pg.draw.rect(self.surface, color, cell, 2)

    def get_cell(self, mouse_pos):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells_rects[i][j].contains(pg.Rect(*mouse_pos, 1, 1)):
                    return i, j
        return None

    def on_click(self, cell):
        self.selected_cell = cell

        info = self.game.sprite_groups["info"]
        if isinstance(info, Info):
            info.kill_sprites()

        x, y = cell
        cell_obj = self.cells_objects[x][y]
        self.game.sprite_groups["info"] = Info(self.game, cell_obj)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def init_level(self):
        level = load_level(self.level)
        for i in range(len(level)):
            for j in range(len(level[i])):
                self.cells_objects[i][j] = load_object(self.game, level[i][j], (j, i))
