import pygame as pg

from .platform import Platform


class Base(Platform):
    IMAGE = "platforms/base.png"
    SPRITE_GROUPS = ["platforms", "base"]

    INFO_HEADER = "БАЗА"
    INFO_DESCRIPTION = "Это ваша база. Защищайте ее от попадания мобов."

    def __init__(self, game, cell):
        super().__init__(game, cell)