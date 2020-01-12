import pygame as pg

from ..gameobject import GameObject
from core.utils import load_image


class Platform(GameObject):
    IMAGE = None
    INFO_IMAGE = "platforms_info/platform.png"

    SPRITE_GROUPS = ["platforms"]

    def __init__(self, game, cell):
        super().__init__(game, game.game_field, cell)

        self.info_image = load_image(self.INFO_IMAGE)