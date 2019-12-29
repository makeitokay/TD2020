import pygame as pg
from .utils import WHITE, BLACK
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Field:
    CELL_SIZE = 50

    def __init__(self, surface):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = surface
        self.cells = [[0] * self.width for _ in range(self.height)]

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = pg.Rect(j * self.CELL_SIZE, i * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                self.cells[i][j] = cell
                pg.draw.rect(self.surface, WHITE, cell, 1)

    def get_cell(self, mouse_pos):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j].contains(pg.Rect(*mouse_pos, 1, 1)):
                    return i, j
        return None