import pygame as pg

from .platform import Platform


class Weapon(Platform):
    IMAGE = "platforms/weapon.png"
    SPRITE_GROUPS = ["platforms", "weapons"]

    def __init__(self, game, cell):
        super().__init__(game, cell)