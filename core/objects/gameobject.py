import pygame as pg
from ..utils import load_image


class GameObject(pg.sprite.Sprite):
    IMAGE = None
    SPRITE_GROUPS = []

    def __init__(self, game, field=None, cell=None, pos=None):
        """
        :param game: экземпляр класса ядра игры
        :param field: объект поля, в котором находится спрайт
        :param cell: клетка поля, в которой располагается спрайт в формате (x, y)
        :param pos: координаты спрайта в явном формате (если он не находится в клетке поля)
        """

        super().__init__(*(game.sprite_groups[g] for g in ('all', *self.SPRITE_GROUPS)))

        self.game = game
        self.field = field
        self.cell = cell

        if self.IMAGE is None:
            self.image = pg.Surface((0, 0))
        else:
            self.image = load_image(self.IMAGE)

        self.rect = self.image.get_rect()
        if cell is None:
            self.rect.x, self.rect.y = pos
        else:
            self.rect.x, self.rect.y = self.field.get_cell_coordinates(cell)

    @property
    def pos(self):
        return self.rect.topleft

    def __sub__(self, other):
        if self.cell:
            cell = other.cell if other.cell else self.field.get_cell(other.pos)
            return abs(self.cell[0] - cell[0]), abs(self.cell[1] - cell[1])
        return abs(self.rect.x - other.rect.x), abs(self.rect.y - other.rect.y)

    def get_center_distance(self, other):
        dx = pow(self.rect.center[0] - other.rect.center[0], 2)
        dy = pow(self.rect.center[1] - other.rect.center[1], 2)
        return pow(dx + dy, 0.5)

    def get_x_center_distance(self, other):
        return abs(self.rect.center[0] - other.rect.center[0])

    def get_y_center_distance(self, other):
        return abs(self.rect.center[1] - other.rect.center[1])