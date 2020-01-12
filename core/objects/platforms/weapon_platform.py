import pygame as pg

from core.objects.platforms.platform import Platform


class WeaponPlatform(Platform):
    IMAGE = "platforms/weapon.png"
    INFO_IMAGE = "platforms_info/weapon.png"

    SPRITE_GROUPS = ["platforms", "weapon_platforms"]

    def __init__(self, game, cell):
        super().__init__(game, cell)