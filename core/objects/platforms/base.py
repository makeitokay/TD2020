import pygame as pg

from .platform import Platform


class Base(Platform):
    IMAGE = "platforms/base.png"
    INFO_IMAGE = "platforms_info/base.png"

    SPRITE_GROUPS = ["platforms", "base"]

    def __init__(self, game, cell):
        super().__init__(game, cell)

    def update(self):
        if pg.sprite.spritecollide(self, self.game.sprite_groups["enemies"], dokill=True):
            self.game.hp -= 1