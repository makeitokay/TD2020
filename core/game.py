import pygame as pg
from .settings import FPS
import random

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.surface.fill((random.randint(0, 255), 100, 100))
        pg.display.update()