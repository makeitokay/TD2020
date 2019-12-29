import pygame as pg
from .utils import WHITE, BLACK
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Field:
    CELL_SIZE = 50

    def __init__(self, surface):
        self.width = SCREEN_WIDTH // self.CELL_SIZE
        self.height = SCREEN_HEIGHT // self.CELL_SIZE
        self.surface = surface
        self.cells = [[0] * self.width for _ in range(self.height)]
        self.colors = [[BLACK] * self.width for _ in range(self.height)]

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = pg.Rect(j * self.CELL_SIZE, i * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                self.cells[i][j] = cell
                pg.draw.rect(self.surface, BLACK, cell, 1)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].contains(pg.Rect(*mouse_pos, 1, 1)):
                    return i, j
        return None

    def on_click(self, cell):
        x, y = cell
        color = BLACK if self.colors[x][y] == WHITE else WHITE
        self.colors[x][y] = color
        pg.draw.rect(self.surface, color, self.cells[x][y])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
