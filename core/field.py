import pygame as pg
from .utils import BLUE, BLACK, get_cell_coordinates
from .settings import FIELD_WIDTH, FIELD_HEIGHT, CELL_SIZE

class Field:
    WIDTH = FIELD_WIDTH
    HEIGHT = FIELD_HEIGHT

    def __init__(self, surface):
        self.surface = surface
        self.cells = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
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
