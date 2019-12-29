import pygame as pg

from core.utils import terminate
from .settings import FPS
from .field import Field

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pg.time.Clock()
        self.field = Field(self.surface)

    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.field.render()
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.field.get_click(event.pos)