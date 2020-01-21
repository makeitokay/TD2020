import pygame as pg

from .gameobject import GameObject
from core.utils import WHITE


class DynamicText(GameObject):
    SPRITE_GROUPS = ["text"]

    def __init__(self, game, pos, text_function, color=WHITE, size=16):
        super().__init__(game, pos=pos)

        self.text_function = text_function
        self.color = color

        self.font = pg.font.Font("data/fonts/RobotoSlab-Regular.ttf", size)
        self.image = self.font.render(str(self.text_function()), True, self.color)

    def update(self):
        self.image = self.font.render(str(self.text_function()), True, self.color)
