import pygame as pg
from ..utils import load_image, get_cell_coordinates


class GameObject(pg.sprite.Sprite):
    IMAGE = None
    SPRITE_GROUPS = []

    def __init__(self, game, cell):
        super().__init__(*(game.sprite_groups[g] for g in ('all', *self.SPRITE_GROUPS)))

        self.game = game
        self.x, self.y = cell

        if self.IMAGE is None:
            self.image = pg.Surface((0, 0))
        else:
            self.image = load_image(self.IMAGE)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = get_cell_coordinates(*cell)