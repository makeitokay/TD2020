import pygame as pg

from core.utils import terminate
from .settings import FPS
from .field import Field

class Game:
    def __init__(self, surface, level=1):
        self.surface = surface
        self.clock = pg.time.Clock()

        self.sprite_groups = {
            "all": pg.sprite.Group(),
            "platforms": pg.sprite.Group(),
            "weapons": pg.sprite.Group(),
            "spawn": pg.sprite.Group(),
            "base": pg.sprite.Group()
        }

        self.field = Field(self, self.surface, level)

    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.field.render()
        self.sprite_groups["all"].update()
        self.sprite_groups["all"].draw(self.surface)

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.field.get_click(event.pos)
