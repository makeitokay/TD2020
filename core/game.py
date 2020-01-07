import pygame as pg

from core.objects.coin_counter import CoinCounter
from core.utils import terminate, load_image
from .settings import FPS, FIELD_WIDTH, CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, FIELD_HEIGHT
from .field import Field


class Game:
    def __init__(self, surface, level=1):
        self.surface = surface
        self.clock = pg.time.Clock()

        self.sprite_groups = {
            "all": pg.sprite.Group(),
            "platforms": pg.sprite.Group(),
            "weapon_platforms": pg.sprite.Group(),
            "spawn": pg.sprite.Group(),
            "base": pg.sprite.Group(),
            "road": pg.sprite.Group(),
            "text": pg.sprite.Group(),
            "weapons": pg.sprite.Group(),

            "info": None
        }

        self.field = Field(self, self.surface, level)

        self.right_block = pg.Surface((SCREEN_WIDTH - FIELD_WIDTH * CELL_SIZE, SCREEN_HEIGHT))

        self.coins = 200
        self.coin_image = load_image("coin.png")
        self.coin_counter = CoinCounter(self)

        self.play_image = load_image("play.png")

    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.field.render()

        self.right_block.fill((0, 0, 0))
        self.surface.blit(self.right_block, (FIELD_WIDTH * CELL_SIZE, 0))

        self.surface.blit(self.coin_image, (95, FIELD_HEIGHT * CELL_SIZE + 40))
        self.surface.blit(self.play_image, (15, FIELD_HEIGHT * CELL_SIZE + 40))

        self.sprite_groups["all"].update()
        self.sprite_groups["all"].draw(self.surface)

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouse_click_handler(event.pos)

    def mouse_click_handler(self, pos):
        cell = self.field.get_cell(pos)
        if cell:
            self.field.on_click(cell)
        else:
            self.field.unselect_cell()

