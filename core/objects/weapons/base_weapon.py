import pygame as pg

from .weapon import Weapon


class BaseWeapon(Weapon):
    SPRITE_GROUPS = ["weapons", "base_weapons"]

    IMAGE = "weapons/base_weapon.png"
    SHOP_IMAGE = "weapon_shop/base_weapon.png"

    NAME = "Базовая"

    COST = 48

    def __init__(self, game, cell):
        super().__init__(game, cell)

        self.damage = 1
        self.radius = 1
        self.attack_speed = 1
        self.move_speed = 5
