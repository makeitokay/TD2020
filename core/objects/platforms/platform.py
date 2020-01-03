import pygame as pg

from ..gameobject import GameObject


class Platform(GameObject):
    IMAGE = None
    SPRITE_GROUPS = ["platforms"]

    INFO_HEADER = "ПУСТАЯ ЯЧЕЙКА"
    INFO_DESCRIPTION = "Пустота."

    def __init__(self, game, cell):
        super().__init__(game, cell)