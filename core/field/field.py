import pygame as pg
from core.utils import load_image


class Field(pg.Surface):
    WIDTH = 0
    HEIGHT = 0
    CELL_SIZE = 50

    CELL_STROKE_IMAGE = None

    SPRITE_GROUPS = []

    def __init__(self, game, pos):
        super().__init__((self.WIDTH * self.CELL_SIZE, self.HEIGHT * self.CELL_SIZE))

        self.game = game
        self.pos = pos

        self.field = [[None] * self.WIDTH for _ in range(self.HEIGHT)]

        self.selected_cell = None
        self.cell_stroke_image = load_image(self.CELL_STROKE_IMAGE)

    @property
    def selected_cell_obj(self):
        if self.selected_cell is None:
            return
        return self.get_cell_obj(self.selected_cell)

    def render(self):
        self.fill((0, 0, 0))
        for group in self.SPRITE_GROUPS:
            self.game.sprite_groups[group].draw(self)
        if self.selected_cell:
            self.blit(self.cell_stroke_image, self.get_cell_rect(self.selected_cell).topleft)

    def get_cell(self, pos):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.get_cell_rect((j, i), in_field=False).contains(pg.Rect(*pos, 1, 1)):
                    return j, i
        return None

    def get_cell_obj(self, cell):
        x, y = cell
        return self.field[y][x]

    def on_click(self, cell):
        # Отменяем выделение клетки только в том случае, если кликнули на другую клетку
        if self.selected_cell != cell:
            self.unselect_cell()

        x, y = cell
        self.selected_cell = (x, y)

    def unselect_cell(self):
        self.selected_cell = None

    # TODO: рефакторинг позиционирования (поле in_field - костыль)

    def get_cell_rect(self, cell, in_field=True):
        """
        :param cell: координаты клетки (x, y)
        :param in_field: если True, вернет прямоугольник клетки в поле
        """
        return pg.Rect(
            self.get_cell_coordinates(cell, in_field), (self.CELL_SIZE, self.CELL_SIZE)
        )

    def get_cell_coordinates(self, cell, in_field=True):
        """
        :param cell: координаты клетки (x, y)
        :param in_field: если True, вернет координаты клетки в поле
        """
        cell_x, cell_y = cell
        field_x, field_y = self.pos

        coords_in_field = cell_x * self.CELL_SIZE, cell_y * self.CELL_SIZE
        if in_field:
            return coords_in_field
        return field_x + coords_in_field[0], field_y + coords_in_field[1]