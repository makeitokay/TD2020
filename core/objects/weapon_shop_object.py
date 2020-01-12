from core.objects.gameobject import GameObject

from os import path

class WeaponShopObject(GameObject):
    SPRITE_GROUPS = ["weapon_shop_objects"]

    def __init__(self, game, cell, weapon_class):
        self.IMAGE = weapon_class.SHOP_IMAGE

        super().__init__(game, game.weapon_shop, cell)

        self.weapon_class = weapon_class