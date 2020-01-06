import pygame as pg

from core.objects.platforms.platform import Platform


class WeaponPlatform(Platform):
    IMAGE = "platforms/weapon.png"
    SPRITE_GROUPS = ["platforms", "weapon_platforms"]

    INFO_HEADER = "ПЛАТФОРМА"
    INFO_DESCRIPTION = "Это платформа. Здесь должны располагаться ваши башни."

    def __init__(self, game, cell):
        super().__init__(game, cell)