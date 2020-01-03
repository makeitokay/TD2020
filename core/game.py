import pygame as pg

from core.utils import terminate
from .settings import FPS, FIELD_WIDTH, CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from .field import Field
from random import randint
# from .text import Text

class Game:
    def __init__(self, surface, level=1):
        self.surface = surface
        self.clock = pg.time.Clock()

        self.sprite_groups = {
            "all": pg.sprite.Group(),
            "platforms": pg.sprite.Group(),
            "weapons": pg.sprite.Group(),
            "spawn": pg.sprite.Group(),
            "base": pg.sprite.Group(),
            "road": pg.sprite.Group(),
            "text": pg.sprite.Group(),

            "info": None
        }

        self.field = Field(self, self.surface, level)

        self.right_block = pg.Surface((SCREEN_WIDTH - FIELD_WIDTH * CELL_SIZE, SCREEN_HEIGHT))

    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.field.render()

        self.right_block.fill((0, 0, 0))
        self.surface.blit(self.right_block, (FIELD_WIDTH * CELL_SIZE, 0))

        self.sprite_groups["all"].update()
        self.sprite_groups["all"].draw(self.surface)

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.field.get_click(event.pos)
