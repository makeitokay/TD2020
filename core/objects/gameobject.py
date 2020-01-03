import pygame as pg
from ..utils import load_image, get_cell_coordinates


class GameObject(pg.sprite.Sprite):
    IMAGE = None
    SPRITE_GROUPS = []

    def __init__(self, game, cell=None, pos=None):
        """
        :param game: экземпляр класса ядра игры
        :param cell: клетка, в которой располагается объект в формате (x, y)
        :param pos: если координаты клетки не передаются, должна передаваться позиция объекта напрямую
        """

        super().__init__(*(game.sprite_groups[g] for g in ('all', *self.SPRITE_GROUPS)))

        self.game = game

        if self.IMAGE is None:
            self.image = pg.Surface((0, 0))
        else:
            self.image = load_image(self.IMAGE)

        self.rect = self.image.get_rect()
        if cell is None:
            self.rect.x, self.rect.y = pos
        else:
            self.rect.x, self.rect.y = get_cell_coordinates(*cell)
