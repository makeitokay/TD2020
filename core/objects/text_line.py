import pygame as pg

from .gameobject import GameObject
from random import randint


class TextLine(GameObject):
    def __init__(self, game, pos, text):
        super().__init__(game, pos=pos)

        self.game = game
        self.pos = pos
        self.text = text

        self.font = pg.font.Font("data/fonts/RobotoSlab-Regular.ttf", 16)
        self.image = self.font.render(self.text, True, (255, 255, 255))
        self.rect.x = self.rect.x - self.image.get_width() // 2

    def update(self):
        self.image = self.font.render(self.text, True, (255, 255, 255))
