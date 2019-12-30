import pygame as pg

from .platform import Platform


class Road(Platform):
    IMAGE = "platforms/road.png"
    SPRITE_GROUPS = ["platforms", "road"]

    def __init__(self, game, cell, way):
        super().__init__(game, cell)

        self.way = way