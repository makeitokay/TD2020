import pygame as pg
from ...gameobject import GameObject


class Weapon(GameObject):
    SPRITE_GROUPS = ["weapons"]
    IMAGE = None

    def __init__(self, game, cell):
        super().__init__(game, cell)

        self.damage = 0
        self.radius = 0
        self.attack_speed = 0
        self.move_speed = 0