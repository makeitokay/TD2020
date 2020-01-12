import pygame as pg

from .platform import Platform


class Road(Platform):
    IMAGE = "platforms/road.png"
    INFO_IMAGE = "platforms_info/road.png"

    SPRITE_GROUPS = ["platforms", "road"]

    WAYS = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1)
    }

    def __init__(self, game, cell, way):
        super().__init__(game, cell)

        self.way = way