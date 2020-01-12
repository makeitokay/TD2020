import pygame as pg
from core.objects.gameobject import GameObject


class Weapon(GameObject):
    SPRITE_GROUPS = ["weapons"]

    IMAGE = None
    SHOP_IMAGE = None

    NAME = None

    def __init__(self, game, cell):
        super().__init__(game, game.game_field, cell)

        self.cost = 0
        self.damage = 0
        self.radius = 0
        self.attack_speed = 0
        self.move_speed = 0