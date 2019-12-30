import pygame as pg
from .utils import BLUE, BLACK, get_cell_coordinates, load_level
from .settings import FIELD_WIDTH, FIELD_HEIGHT, CELL_SIZE
from .objects.platforms.platform import Platform
from .objects.platforms.weapon import Weapon
from .objects.platforms.spawn import Spawn
from .objects.platforms.base import Base
from .objects.platforms.road import Road

class Field:
    WIDTH = FIELD_WIDTH
    HEIGHT = FIELD_HEIGHT

    def __init__(self, game, surface, level=1):
        self.game = game
        self.surface = surface
        self.level = level

        self.cells = [[0] * self.WIDTH for _ in range(self.HEIGHT)]

        self.init_level()

        self.colors = [[BLACK] * self.WIDTH for _ in range(self.HEIGHT)]

    def render(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                cell = pg.Rect(*get_cell_coordinates(j, i), CELL_SIZE, CELL_SIZE)
                self.cells[i][j] = cell
                pg.draw.rect(self.surface, self.colors[i][j], cell, 2)

    def get_cell(self, mouse_pos):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.cells[i][j].contains(pg.Rect(*mouse_pos, 1, 1)):
                    return i, j
        return None

    def on_click(self, cell):
        x, y = cell
        color = BLACK if self.colors[x][y] == BLUE else BLUE
        self.colors[x][y] = color

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def init_level(self):
        level = load_level(self.level)
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == "w":
                    self.cells[i][j] = Weapon(self.game, (j, i))
                elif level[i][j] == "s":
                    self.cells[i][j] = Spawn(self.game, (j, i))
                elif level[i][j] == "b":
                    self.cells[i][j] = Base(self.game, (j, i))
                elif level[i][j] in (">", "v", "<", "^"):
                    self.cells[i][j] = Road(self.game, (j, i), way=level[i][j])
                else:
                    self.cells[i][j] = Platform(self.game, (j, i))