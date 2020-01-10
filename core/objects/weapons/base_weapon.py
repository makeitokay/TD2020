import pygame as pg

from .weapon import Weapon


class BaseWeapon(Weapon):
    SPRITE_GROUPS = ["weapons", "base_weapons"]
    IMAGE = "weapons/base_weapon.png"

    NAME = "Базовая"

    def __init__(self, game, cell):
        super().__init__(game, cell)

        self.cost = 48