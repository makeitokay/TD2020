import pygame as pg

from .settings import SCREEN_WIDTH, FIELD_WIDTH, CELL_SIZE, SCREEN_HEIGHT
from .utils import load_image, scale_image

from .objects.weapons import WEAPONS
from .objects.text_line import TextLine


class WeaponShop(pg.Surface):
    X_INTERVAL = 30
    Y_INTERVAL = 30

    ROW_AMOUNT = 5

    def __init__(self, game):
        super().__init__((SCREEN_WIDTH - FIELD_WIDTH * CELL_SIZE, SCREEN_HEIGHT - 100))

        self.game = game

        self.fill_weapons()

    def fill_weapons(self):
        y = 0
        for i in range(len(WEAPONS) // self.ROW_AMOUNT + 1):
            x = 0
            for n in range(self.ROW_AMOUNT):
                current_index = i * self.ROW_AMOUNT + n
                if current_index == len(WEAPONS):
                    break

                image = scale_image(load_image(WEAPONS[current_index].IMAGE), 1.5)
                text = TextLine(self.game,
                                pos=(FIELD_WIDTH * CELL_SIZE + x, 100 + y),
                                text=WEAPONS[current_index].NAME)
                self.blit(image, (x, y))

                x += self.X_INTERVAL
            y += self.Y_INTERVAL