import pygame as pg
from .text_line import TextLine
from ..settings import RIGHT_BLOCK_CENTERX_POSITION, FIELD_WIDTH, CELL_SIZE

class Info(pg.sprite.Group):
    INFO_HEADER_POS = (RIGHT_BLOCK_CENTERX_POSITION, 20)
    INFO_DESCRIPTION_POS = (RIGHT_BLOCK_CENTERX_POSITION, 50)


    def __init__(self, game, cell_obj):
            self.game = game

            sprites = [
                TextLine(self.game, self.INFO_HEADER_POS, cell_obj.INFO_HEADER),
                TextLine(self.game, self.INFO_DESCRIPTION_POS, cell_obj.INFO_DESCRIPTION)
            ]

            super().__init__(*sprites)

    def kill_sprites(self):
        for sprite in self.sprites():
            sprite.kill()
