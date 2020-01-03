import pygame as pg

from .platform import Platform


class Weapon(Platform):
    IMAGE = "platforms/weapon.png"
    SPRITE_GROUPS = ["platforms", "weapons"]

    INFO_HEADER = "ПЛАТФОРМА"
    INFO_DESCRIPTION = "Это платформа. Здесь должны располагаться ваши башни."

    def __init__(self, game, cell):
        super().__init__(game, cell)