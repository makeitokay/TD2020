import pygame as pg

from .platform import Platform


class Road(Platform):
    IMAGE = "platforms/road.png"
    SPRITE_GROUPS = ["platforms", "road"]

    INFO_HEADER = "ДОРОГА"
    INFO_DESCRIPTION = "Обычная дорога, ничего особенного."

    def __init__(self, game, cell, way):
        super().__init__(game, cell)

        self.way = way