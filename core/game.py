import pygame as pg

from .settings import FPS
from .field import Field

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pg.time.Clock()
        self.field = Field(self.surface)
        self.field.render()

    def run(self):
        while True:
            self.update()
            self.clock.tick(FPS)

    def update(self):
        pg.display.update()