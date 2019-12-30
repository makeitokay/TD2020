import pygame as pg

from ..gameobject import GameObject

class Platform(GameObject):
    IMAGE = None
    SPRITE_GROUPS = ["platforms"]

    def __init__(self, game, cell):
        super().__init__(game, cell)