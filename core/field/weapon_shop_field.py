import pygame as pg

from core.objects.weapons import WEAPONS
from core.objects.weapon_shop_object import WeaponShopObject

from core.field.field import Field


class WeaponShopField(Field):
    WIDTH = 5
    HEIGHT = 2
    CELL_SIZE = 100

    CELL_STROKE_IMAGE = "weapon_shop_cell_stroke.png"

    SPRITE_GROUPS = ["weapon_shop_objects"]

    def __init__(self, game, pos):
        super().__init__(game, pos)

        self.game = game

    def init_shop(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                index = i * self.HEIGHT + j
                if index == len(WEAPONS):
                    return
                self.field[i][j] = WeaponShopObject(self.game, (i, j), WEAPONS[index])
