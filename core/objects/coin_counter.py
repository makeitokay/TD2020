import pygame as pg

from core.settings import GAME_FIELD_HEIGHT, CELL_SIZE
from .gameobject import GameObject


class CoinCounter(GameObject):

    def __init__(self, game):
        super().__init__(game, pos=(150, GAME_FIELD_HEIGHT * CELL_SIZE + 40))

        self.font = pg.font.Font("data/fonts/RobotoSlab-Regular.ttf", 32)
        self.image = pg.Surface((100, 100))

    def update(self):
        self.image = self.font.render(str(self.game.coins), True, (255, 188, 0))